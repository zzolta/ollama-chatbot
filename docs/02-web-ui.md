Status: implementation

## Overview

Replace the terminal interface with a Gradio web UI so the user opens the chatbot in a browser instead of a command prompt. The temperature selector becomes a slider. All existing chat behaviour is preserved.

## User Stories

- As a user, I want to open the chatbot in my browser without using the terminal
- As a user, I want to set the temperature via a slider before or during the chat
- As a user, I want to see warnings about extreme temperature values directly in the UI
- As a user, I want the conversation history to persist for the session as before

## UI/UX Flow

```
Browser opens at http://localhost:7860

┌─────────────────────────────────────┐
│  Ollama Chatbot                     │
│─────────────────────────────────────│
│  [chat history area]                │
│                                     │
│  You: Hello                         │
│  Bot: Hello! How can I help?        │
│                                     │
│─────────────────────────────────────│
│  [message input]        [Send]      │
│─────────────────────────────────────│
│  Temperature  0.0 ──●────────── 1.0 │
│  (warning shown at 0 and 1)         │
└─────────────────────────────────────│
```

## Technical Approach

| Decision | Choice |
|----------|--------|
| Web framework | Gradio — purpose-built for ML/chat demos, zero HTML/CSS |
| Entry point | `chatbot.py` rewritten (single file kept) |
| Temperature input | `gr.Slider(0.0, 1.0, value=0.7)` via `additional_inputs` |
| Temperature warnings | `gr.Markdown` component updated via slider change event |
| History format | Gradio `type="messages"` — maps directly to Ollama message dicts |
| Launch | `demo.launch()` — opens at `http://localhost:7860` |

## Test Scenarios

1. **App starts** — running `python chatbot.py` opens browser at `http://localhost:7860`
2. **Default temperature** — slider starts at `0.7`, no warning shown
3. **Temperature 0 warning** — moving slider to `0` shows greedy-decoding warning
4. **Temperature 0.5 info** — moving slider to `0.5` shows "good average" message
5. **Temperature 1 warning** — moving slider to `1` shows raw-distribution warning
6. **Chat response** — sending a message produces a bot reply in the chat window
7. **Memory** — follow-up message referencing the previous turn is answered correctly
8. **Empty input** — sending empty message produces no response

## Out of Scope

- Authentication or multi-user sessions
- Persistent history across page reloads
- Model selection in the UI
- Streaming token-by-token output
- Dark mode or custom theming
- Deployment beyond localhost

## Files in Scope

- `chatbot.py`
- `USER_GUIDE.md`
- `docs/02-web-ui.md`
- `docs/index.md`
