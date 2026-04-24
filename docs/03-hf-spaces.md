Status: implementation

## Overview

Deploy the chatbot publicly for free using Hugging Face Spaces. The local Ollama backend is replaced with the HF Serverless Inference API (Qwen/Qwen2.5-7B-Instruct). The Gradio UI is unchanged — only the backend changes.

## User Stories

- As a user, I want to access the chatbot from a public URL without installing anything
- As a developer, I want the app to run on free infrastructure with no ongoing cost
- As a developer, I want to run the app locally using the same code by setting an env var

## Technical Approach

| Decision | Choice |
|----------|--------|
| Hosting | Hugging Face Spaces (free tier) |
| Model | `Qwen/Qwen2.5-7B-Instruct` — Apache 2.0, 128K context, GPT-3.5 class |
| Backend client | `huggingface_hub.InferenceClient` |
| Auth | `HF_TOKEN` env var (Space Secret in production) |
| Space config | `README.md` YAML frontmatter |

## Deployment Steps (manual)

1. Create a new HF Space at `huggingface.co/new-space` → SDK: Gradio
2. Add this repo as a git remote and push
3. Add `HF_TOKEN` as a Space Secret (Settings → Variables and secrets)
4. Space builds automatically and goes live

## Test Scenarios

1. **Local run** — `HF_TOKEN=hf_... python chatbot.py` opens browser, responses come from Qwen2.5-7B
2. **Multi-turn memory** — follow-up referencing a previous message is answered correctly
3. **Temperature warnings** — slider at 0, 0.5, 1.0 shows correct messages
4. **HF Spaces** — pushing to the Space produces a live public URL

## Out of Scope

- Custom domain
- Authentication / access control
- Persistent history across sessions
- Streaming output
- Upgrading to paid HF tier

## Files in Scope

- `chatbot.py`
- `requirements.txt`
- `README.md`
- `USER_GUIDE.md`
- `docs/03-hf-spaces.md`
- `docs/index.md`
- `CLAUDE.md`
