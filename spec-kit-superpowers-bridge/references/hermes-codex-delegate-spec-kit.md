# Hermes to Codex Delegation for Spec Kit Work

Use this reference when Hermes launches Codex through the in-repo `codex-delegate` skill for a Spec Kit feature.

## Decision

Delegate to Codex when the active Spec Kit feature has a clear `spec.md`, `plan.md`, or `tasks.md` slice and the work is large enough to justify a separate implementation lane.

Do not delegate when the next step is still product clarification. Run the relevant Spec Kit phase first.

## Prompt Skeleton

Build `prompt.md` for `codex-delegate` with this structure:

```markdown
You are running as Codex CLI on the user's Windows machine.

Task:
Implement this bounded slice from the active Spec Kit feature:
<exact task ids or feature slice>

Working directory:
<absolute repo path>

Current worktree status before you start:
<git status --short output>

Spec Kit source of truth:
- Constitution: `.specify/memory/constitution.md`
- Feature: `specs/NNN-feature-name/`
- Spec: `specs/NNN-feature-name/spec.md`
- Plan: `specs/NNN-feature-name/plan.md`
- Tasks: `specs/NNN-feature-name/tasks.md`
- Checklists/contracts/data models: <paths if present>

Read those files before editing. If any artifact conflicts with the latest user instruction, stop and report the conflict instead of guessing.

Acceptance criteria:
- <copy concise criteria from spec/tasks>

Method requirements:
- Preserve user changes. Do not revert unrelated edits.
- Follow Superpowers discipline: TDD for behavior changes, systematic debugging for bugs, focused implementation, verification-before-completion.
- Keep changes scoped to the active Spec Kit task slice.
- Do not mark tasks complete unless implementation and verification evidence exist.
- If requirements change, report the needed Spec Kit artifact update rather than silently drifting.

Operating rules:
- Hermes owns orchestration and final acceptance.
- Do not call Hermes kanban, Telegram, gateway, or board lifecycle tools.
- Do not create or commit run artifacts such as `final.md`, `events.jsonl`, `stderr.log`, `exit-code.txt`, or `prompt.md` inside the repository.
- Do not reveal secrets from `.env`, auth files, tokens, browser profiles, or credential stores.

Verification:
- Run: `<targeted command>`
- If broad verification is too expensive, run the smallest command that proves the task and explain what remains unverified.

Final response must include:
- Summary
- Files changed
- Verification commands and observed results
- Any Spec Kit artifact drift or remaining risk
```

## Hermes Reconciliation

After Codex exits, Hermes must inspect:

```bash
git status --short
git diff --stat
git diff -- <targeted files>
```

Then read the Codex run directory:

- `exit-code.txt`
- `final.md`
- tail of `events.jsonl`
- `stderr.log` only when nonzero exit or suspicious behavior exists

Hermes may accept, partially accept, or reject the Codex diff. A zero exit code is not enough by itself.

## Task Status Rules

Only mark a Spec Kit task complete when all are true:

- The expected files changed.
- The task's acceptance criteria are covered.
- Verification was run or the skipped verification is explicitly justified.
- No unrelated run artifacts or generated caches are in the repo diff.

If the implementation exposes a wrong or incomplete spec, update or request an update to `spec.md`, `plan.md`, or `tasks.md` before continuing dependent work.
