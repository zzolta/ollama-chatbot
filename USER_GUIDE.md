# User Guide — Ollama Chatbot

## Starting the App

```bash
python chatbot.py
```

## Setting the Temperature

On startup you will be asked to choose a temperature:

```
Enter temperature (0.0 - 1.0) or press Enter to use default [0.7]:
```

Temperature controls how creative or consistent the model's responses are.

| Value | Behaviour |
|-------|-----------|
| `0`   | Greedy decoding — maximally consistent, may feel repetitive |
| `0.5` | Good average, less creative than default |
| `0.7` | Default — balanced creativity and consistency |
| `1.0` | Raw probability distribution — more varied, may feel unpredictable |

Press **Enter** without typing anything to use the default (`0.7`). Any value outside `0.0–1.0` is clamped automatically. Invalid text falls back to `0.7`.

## Chatting

Type your message and press **Enter**. The bot will respond.

```
You: What is the capital of France?
Bot: The capital of France is Paris.
```

The conversation history is kept for the entire session, so the model remembers what was said earlier in the same chat.

## Exiting

Type `quit`, `exit`, or `q` and press **Enter**.
