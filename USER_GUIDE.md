# User Guide — Ollama Chatbot

## Starting the App

```bash
python chatbot.py
```

The app will open automatically in your browser at `http://localhost:7860`.

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

The conversation history is kept for the entire session, so the model remembers what was said earlier in the same chat.

## Exiting

Close the browser tab and stop the terminal process with `Ctrl+C`.
