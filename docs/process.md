# Development Process

Structured methodology for developing this application using AI coding assistants. Every feature goes through three phases with a quality gate between each.

---

## Phase 1: Exploration

**Goal:** Finalise requirements before any production code begins.

- Collaborate on feature ideas and cut non-essential scope
- Define concrete test scenarios with observable results
- Document everything in a PRD: `docs/<number>-<feature-name>.md`

**PRD must include:**
- Overview (2–3 sentences)
- User stories
- UI/UX flows
- Technical approach with key decisions
- Test scenarios with expected observable results
- Explicit out-of-scope items
- Files in Scope list

Set PRD `Status` field to `exploration`.

**Gate:** User reviews and approves the PRD before moving on.

---

## Phase 2: Implementation

**Goal:** Build exactly what the PRD specifies — nothing more.

- AI references the PRD, restates scope, and lists assumptions before coding
- Write code and tests together
- User manually tests every PRD test scenario end-to-end

Set PRD `Status` field to `implementation`.

**Gate:** User reviews code and approves before moving on.

---

## Phase 3: Refactoring

**Goal:** Clean up and simplify without changing observable behaviour.

- Consolidate, optimise, and remove dead code
- Must not change UI, routes, persisted data shapes, or public interfaces
- All tests must remain green

Set PRD `Status` field to `refactoring`, then `done` when complete.

**Gate:** User reviews and approves before closing the feature.

---

## Principles

- No production code until the PRD is signed off
- If it is not in the PRD, it does not get built
- AI never commits — user signs off and commits at each gate
- Never paste secrets or keys into prompts or code
- Keep scope tight — cut anything non-essential
