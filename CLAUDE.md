# Ollama Chatbot

A minimal Python terminal chatbot using a locally-running Ollama LLM.

## Process

Follow `docs/process.md`. Every feature goes through:
**Exploration → Implementation → Refactoring** with a user quality gate between phases.

- PRDs: `docs/<number>-<feature-name>.md`
- Repo index: `docs/index.md`
- No production code until the PRD is signed off
- If it is not in the PRD, it does not get built
- AI never commits — user signs off and commits at each gate

## Project Structure

- `chatbot.py` — main entry point, entire application
- `PRD.md` — legacy plan (superseded by `docs/01-ollama-chatbot.md`)
- `USER_GUIDE.md` — end-user documentation
- `docs/process.md` — SDLC process
- `docs/index.md` — repo index
- `docs/01-ollama-chatbot.md` — active PRD

## Prerequisites

- Python with the `ollama` package installed (`pip install ollama`)
- Ollama running locally at `http://localhost:11434`
- Model `gemma4:e2b` pulled (`ollama pull gemma4:e2b`)

## Running

```bash
python chatbot.py
```

Type a message and press Enter to chat. Type `quit`, `exit`, or `q` to stop.

## Rules

Whenever `chatbot.py` is modified due to a changed or new requirement, update `docs/01-ollama-chatbot.md` to reflect the change — add/update requirements and adjust implementation steps accordingly.

Whenever a change affects the user-facing behaviour (prompts, warnings, input handling, exit commands, or any interaction the user sees), update `USER_GUIDE.md` accordingly. This is mandatory.

## Key Details

- Model: `gemma4:e2b`
- Ollama host: `http://localhost:11434`
- Conversation history is kept in memory for the duration of the session (no persistence between runs)
