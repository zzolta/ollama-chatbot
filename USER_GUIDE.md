# User Guide — AI Chatbot

## Using the Hosted App

The chatbot is publicly available on Hugging Face Spaces — no installation needed. Open the Space URL in your browser and start chatting.

## Running Locally

**Windows (CMD):**
```cmd
set HF_TOKEN=hf_your_token_here
set TAVILY_API_KEY=tvly-your-key-here
python chatbot.py
```

**Mac/Linux:**
```bash
export HF_TOKEN=hf_your_token_here
export TAVILY_API_KEY=tvly-your-key-here
python chatbot.py
```

The app opens automatically at `http://localhost:7860`. You need:
- A free Hugging Face token at `huggingface.co/settings/tokens` (Inference Providers permission)
- A free Tavily API key at `app.tavily.com` (1000 searches/month on free tier)

## Setting the Temperature

Use the **Temperature** slider at the bottom of the chat window to control how creative or consistent the model's responses are.

| Value | Behaviour |
|-------|-----------|
| `0`   | Greedy decoding — maximally consistent, may feel repetitive |
| `0.5` | Good average, less creative than default |
| `0.7` | Default — balanced creativity and consistency |
| `1.0` | Raw probability distribution — more varied, may feel unpredictable |

A warning or info message appears below the slider when you select `0`, `0.5`, or `1.0`.

## Chatting

Type your message in the input box at the bottom and press **Enter** or click **Submit**. The bot will respond in the chat window.

The chatbot automatically searches the internet when your question requires current or real-time information (e.g. news, weather, recent events). No need to ask it to search — it decides on its own.

The conversation history is kept for the entire session, so the model remembers what was said earlier in the same chat.

## Exiting (local)

Close the browser tab and stop the terminal process with `Ctrl+C`.
