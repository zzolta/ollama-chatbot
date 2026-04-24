import gradio as gr
import ollama

MODEL = "gemma4:e2b"
client = ollama.Client(host="http://localhost:11434")

WARNINGS = {
    0.0: "Warning: temperature 0 means greedy decoding — responses will be maximally consistent but may feel repetitive.",
    0.5: "Good average, but less creative than default.",
    1.0: "Warning: temperature 1 uses the raw probability distribution — responses may be more varied or unpredictable.",
}

def get_warning(temperature):
    return WARNINGS.get(temperature, "")

def chat(message, history, temperature):
    messages = []
    for m in history:
        text = "".join(part["text"] for part in m["content"] if part.get("type") == "text")
        messages.append({"role": m["role"], "content": text})
    messages.append({"role": "user", "content": message})
    response = client.chat(model=MODEL, messages=messages, options={"temperature": temperature})
    return response.message.content

with gr.Blocks(title="Ollama Chatbot") as demo:
    gr.Markdown("# Ollama Chatbot")
    chatbot = gr.ChatInterface(
        chat,
        additional_inputs=[
            gr.Slider(0.0, 1.0, value=0.7, step=0.1, label="Temperature"),
        ],
    )
    warning = gr.Markdown("")
    chatbot.additional_inputs[0].change(get_warning, chatbot.additional_inputs[0], warning)

demo.launch()
