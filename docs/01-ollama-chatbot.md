Status: done

## Overview

A minimal Python terminal chatbot backed by a locally-running Ollama model. The user selects a temperature on startup and then chats in a loop, with full conversation history maintained for the session.

## User Stories

- As a user, I want to start the chatbot from the terminal and immediately be ready to chat
- As a user, I want to choose the model's temperature at startup so I can explore its effect on responses
- As a user, I want the chatbot to remember what was said earlier in the session
- As a user, I want to exit cleanly by typing a simple command

## UI/UX Flow

```
$ python chatbot.py
Chatbot ready! Type 'quit' to exit.
Enter temperature (0.0 - 1.0) or press Enter to use default [0.7]: 0.5
Good average, but less creative than default.
Using temperature: 0.5

You: Hello
Bot: Hello! How can I help you today?

You: quit
$
```

## Technical Approach

| Decision | Choice |
|----------|--------|
| Ollama client | Official `ollama` Python library (not raw HTTP) |
| Model | `gemma4:e2b` |
| Ollama host | `http://localhost:11434` |
| Conversation memory | In-memory `messages` list, scoped to the session |
| Temperature input | Prompted at startup, clamped to `[0.0, 1.0]`, default `0.7` |

## Test Scenarios

1. **Startup** — running `python chatbot.py` prints the ready message and temperature prompt
2. **Default temperature** — pressing Enter without input sets temperature to `0.7`
3. **Temperature 0 warning** — entering `0` prints a greedy-decoding warning
4. **Temperature 0.5 info** — entering `0.5` prints the "good average" message
5. **Temperature 1 warning** — entering `1` prints a raw-distribution warning
6. **Invalid temperature** — entering non-numeric text falls back to `0.7`
7. **Chat response** — typing a message produces a bot reply
8. **Memory** — a follow-up message referencing the previous turn is answered correctly
9. **Empty input** — pressing Enter without text produces no response and loops
10. **Exit** — typing `quit`, `exit`, or `q` terminates the process cleanly

## Out of Scope

- Persistent conversation history across sessions
- Multiple model selection at runtime
- Web or GUI interface
- Streaming output
- System prompt configuration

## Files in Scope

- `chatbot.py`
- `PRD.md`
- `USER_GUIDE.md`
- `CLAUDE.md`
- `docs/01-ollama-chatbot.md`
