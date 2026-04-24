import json
import os
import gradio as gr
from huggingface_hub import InferenceClient
from tavily import TavilyClient

MODEL = "Qwen/Qwen2.5-7B-Instruct"
hf_client = InferenceClient(model=MODEL, token=os.getenv("HF_TOKEN"))
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

WARNINGS = {
    0.0: "Warning: temperature 0 means greedy decoding — responses will be maximally consistent but may feel repetitive.",
    0.5: "Good average, but less creative than default.",
    1.0: "Warning: temperature 1 uses the raw probability distribution — responses may be more varied or unpredictable.",
}

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the internet for current or real-time information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

SYSTEM_PROMPT = (
    "You are a helpful assistant. "
    "Use the web_search tool when the user asks about current events, recent news, "
    "real-time data, or anything that requires up-to-date information."
)

def web_search(query: str) -> str:
    result = tavily_client.search(query=query, max_results=5, include_answer=True)
    snippets = "\n\n".join(
        f"[{r['title']}]({r['url']})\n{r['content'][:300]}"
        for r in result["results"]
    )
    answer = result.get("answer", "")
    return f"{answer}\n\n{snippets}".strip()

def get_warning(temperature):
    return WARNINGS.get(temperature, "")

def chat(message, history, temperature):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for m in history:
        text = "".join(part["text"] for part in m["content"] if part.get("type") == "text")
        messages.append({"role": m["role"], "content": text})
    messages.append({"role": "user", "content": message})

    response = hf_client.chat_completion(
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
        max_tokens=1024,
        temperature=temperature,
    )

    response_message = response.choices[0].message

    if not response_message.tool_calls:
        return response_message.content

    # Model requested a search — execute and get final answer
    messages.append(response_message)
    for tool_call in response_message.tool_calls:
        args = json.loads(tool_call.function.arguments)
        result = web_search(args["query"])
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": result,
        })

    final = hf_client.chat_completion(messages=messages, max_tokens=1024, temperature=temperature)
    return final.choices[0].message.content

with gr.Blocks(title="AI Chatbot") as demo:
    gr.Markdown("# AI Chatbot")
    chatbot = gr.ChatInterface(
        chat,
        additional_inputs=[
            gr.Slider(0.0, 1.0, value=0.7, step=0.1, label="Temperature"),
        ],
    )
    warning = gr.Markdown("")
    chatbot.additional_inputs[0].change(get_warning, chatbot.additional_inputs[0], warning)

demo.launch()
