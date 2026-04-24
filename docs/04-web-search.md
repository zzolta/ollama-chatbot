Status: implementation

## Overview

Add internet search to the chatbot using Qwen2.5-7B's native tool-calling support and the Tavily search API. The model decides autonomously whether a web search is needed based on the user's prompt. No UI changes — search happens transparently in the backend.

## User Stories

- As a user, I want the chatbot to answer questions about current events with up-to-date information
- As a user, I do not want to trigger searches manually — the chatbot should decide when to search
- As a user, I want the chatbot to answer simple questions directly without unnecessary searches

## Technical Approach

| Decision | Choice |
|----------|--------|
| Search API | Tavily (free tier: 1000 calls/month) |
| Tool calling | Qwen2.5-7B native tool calling via `chat_completion(tools=..., tool_choice="auto")` |
| Auth | `TAVILY_API_KEY` env var (Space Secret in HF Spaces) |
| Search trigger | Model decides via `tool_choice="auto"` |
| Results format | Tavily answer summary + top 5 snippets with title, URL, 300-char content |

## Flow

1. User sends message
2. `chat_completion()` called with `tools=[web_search]`, `tool_choice="auto"`
3. If model returns `tool_calls` → execute Tavily search → feed results back → get final answer
4. If no `tool_calls` → return answer directly

## Test Scenarios

1. **Search triggered** — asking "What is the weather in Budapest today?" triggers a web search and returns current data
2. **No search** — asking "What is 2+2?" returns a direct answer without calling the search tool
3. **Multi-turn with search** — follow-up question after a search-based answer is handled correctly
4. **Temperature slider** — still works as before

## Out of Scope

- Multiple simultaneous tool calls per turn
- Search result caching
- Showing the user which searches were performed
- Limiting search quota per user

## Files in Scope

- `chatbot.py`
- `requirements.txt`
- `docs/04-web-search.md`
- `USER_GUIDE.md`
- `docs/index.md`
- `CLAUDE.md`
