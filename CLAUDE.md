# AI Chatbot

A Gradio web chatbot backed by Qwen/Qwen2.5-7B-Instruct via the HF Serverless Inference API. Deployable on Hugging Face Spaces for free public access.

## Process

Follow `docs/process.md`. Every feature goes through:
**Exploration → Implementation → Refactoring** with a user quality gate between phases.

- PRDs: `docs/<number>-<feature-name>.md`
- Repo index: `docs/index.md`
- No production code until the PRD is signed off
- If it is not in the PRD, it does not get built
- AI never commits — user signs off and commits at each gate

## Project Structure

- `chatbot.py` — main entry point, Gradio web chatbot
- `requirements.txt` — Python dependencies (`gradio`, `huggingface_hub`)
- `README.md` — HF Spaces configuration (YAML frontmatter)
- `PRD.md` — legacy plan (superseded by `docs/01-ollama-chatbot.md`)
- `USER_GUIDE.md` — end-user documentation
- `docs/process.md` — SDLC process
- `docs/index.md` — repo index
- `docs/01-ollama-chatbot.md` — initial chatbot PRD (done)
- `docs/02-web-ui.md` — web UI PRD (done)
- `docs/03-hf-spaces.md` — active PRD (HF Spaces deployment)

## Prerequisites (local)

- Python with dependencies: `pip install -r requirements.txt`
- HF API token: `export HF_TOKEN=hf_...` (get from `huggingface.co/settings/tokens`)

## Running

**Windows (CMD):**
```cmd
set HF_TOKEN=hf_your_token_here
python chatbot.py
```

**Mac/Linux:**
```bash
export HF_TOKEN=hf_your_token_here
python chatbot.py
```

## Rules

Whenever `chatbot.py` is modified due to a changed or new requirement, update the active PRD in `docs/` to reflect the change — add/update requirements and adjust implementation steps accordingly.

Whenever a change affects the user-facing behaviour (prompts, warnings, input handling, or any interaction the user sees), update `USER_GUIDE.md` accordingly. This is mandatory.

## Key Details

- Model: `Qwen/Qwen2.5-7B-Instruct`
- Backend: HF Serverless Inference API via `huggingface_hub.InferenceClient`
- Auth: `HF_TOKEN` environment variable (Space Secret in HF Spaces)
- Conversation history is kept in memory for the duration of the session (no persistence between runs)
