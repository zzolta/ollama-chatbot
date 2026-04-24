# Product Requirements Document — Ollama Chatbot

## Goal

A minimal Python terminal chatbot backed by a local Ollama model, with persistent conversation memory across turns.

## Requirements

1. Use the official `ollama` Python library (not raw HTTP)
2. Target a specific local model — `gemma4:e2b`
3. Connect to Ollama at `http://localhost:11434`
4. Maintain full conversation history so the model has context across turns
5. Skip blank input silently
6. Exit cleanly on `quit`, `exit`, or `q`
7. Print a ready message on startup
8. Prompt user for temperature at startup (default `0.7`, clamped to `0.0–1.0`)
9. Warn the user when temperature is set to `0` (greedy/repetitive) or `1` (raw distribution/unpredictable); inform the user when set to `0.5` (good average, less creative than default)

## Implementation Steps

1. Import `ollama`, define `MODEL` constant and instantiate `ollama.Client`
2. Print startup message
3. Prompt user for temperature; parse and clamp to `[0.0, 1.0]`; default to `0.7` on empty or invalid input
4. Warn if temperature is `0` or `1`
5. Initialize an empty `messages` list
6. Enter infinite loop — read and strip user input
7. Check for exit keywords → `break`; check for empty → `continue`
8. Append `{"role": "user", "content": ...}` to messages
9. Call `client.chat(model=MODEL, messages=messages, options={"temperature": temperature})`
10. Extract `response.message.content`, append as `{"role": "assistant", ...}`
11. Print `Bot: <reply>`

## Output

Single file: `chatbot.py`
