---
name: spec-kit-superpowers-bridge
description: Use when coding work should combine GitHub Spec Kit, Superpowers, Codex CLI, Hermes Agent, Arena Agent Mode, .specify artifacts, speckit commands, or Hermes codex-delegate delegation.
---

# Spec Kit Superpowers Bridge

## Overview

Use Spec Kit as the durable product and planning layer, Superpowers as the engineering method layer, and Codex/Hermes as execution surfaces.

The default split is:

| Layer | Owns |
| --- | --- |
| Spec Kit | `.specify/` governance, feature specs, plans, tasks, checklists, cross-artifact consistency |
| Superpowers | brainstorming, TDD, systematic debugging, review, verification, worktree discipline |
| Codex | direct repository implementation and verification loop |
| Hermes | user conversation, orchestration, background Codex delegation, final reconciliation |

Do not treat these systems as competitors. Spec Kit records intent. Superpowers controls behavior. Codex changes the repo. Hermes coordinates and verifies when it delegates.

## When to Use

Use this skill when:

- The user asks for Spec Kit, speckit, SDD, `.specify`, constitution, spec, plan, tasks, or executable specifications.
- The user asks how to combine Spec Kit with Superpowers.
- Codex is working inside a repo that already has `.specify/` or `specs/NNN-*`.
- Hermes should delegate a Spec Kit feature implementation to Codex through `codex-delegate`.
- A long feature needs durable state across sessions, agents, or handoffs.

Do not use this skill for:

- Tiny one-file fixes where a full spec would be overhead.
- Pure Q&A about Spec Kit with no local workflow impact.
- A repository where the user has not approved adding `.specify/` files.

## Arena Agent Mode

When working in Arena, read `references/arena.md` first. It adapts this workflow to Arena without requiring Codex, Hermes, or native skill invocation.

## Installation and Project Setup

Spec Kit CLI is global, but Spec Kit artifacts are per repository.

Check the CLI:

```powershell
specify version
specify integration list
```

Install the supported CLI when it is missing or stale:

```powershell
uv tool install specify-cli
```

Initialize a repository for Codex skills mode:

```powershell
git status --short
specify init . --integration codex --integration-options="--skills" --script ps
```

Use `--force` only after checking `git status --short` and confirming that merging Spec Kit scaffolding into a non-empty repo is intended.

Expected project artifacts:

```text
.specify/
  memory/constitution.md
  scripts/powershell/
  templates/
.agents/skills/speckit-*/
specs/NNN-feature-name/
  spec.md
  plan.md
  tasks.md
```

Codex invokes Spec Kit project skills as `$speckit-constitution`, `$speckit-specify`, `$speckit-clarify`, `$speckit-plan`, `$speckit-tasks`, `$speckit-analyze`, `$speckit-checklist`, and `$speckit-implement` when those project skills exist.

Hermes usually does not need those Codex project skills directly. Hermes should read and preserve the same `.specify/` and `specs/` artifacts, then use its in-repo `codex-delegate` skill when Codex should execute the heavy loop.

## Source of Truth

Apply this priority order:

1. Latest user instruction and explicit safety constraints.
2. Repo-local agent instructions such as `AGENTS.md`, `CLAUDE.md`, `.rules`, or Hermes skill instructions.
3. Spec Kit constitution at `.specify/memory/constitution.md`.
4. Active feature artifacts in `specs/NNN-*/`: `spec.md`, `plan.md`, `tasks.md`, checklists, contracts, data models.
5. Superpowers method requirements.
6. Existing code patterns.

If implementation reality conflicts with `spec.md` or `plan.md`, do not silently drift. Either update the Spec Kit artifacts through the appropriate Spec Kit phase or report the conflict and ask for direction.

## Standard Flow

Use this flow for medium or large feature work:

1. Confirm the repo and current git state.
2. If `.specify/` is missing, initialize Spec Kit only after the user approves adding project scaffolding.
3. Establish or update the constitution once:

```text
$speckit-constitution Create project principles for code quality, test discipline, UX consistency, security, performance, and change governance.
```

4. Create or update a feature spec:

```text
$speckit-specify <what to build and why; avoid tech-stack detail here>
```

5. Clarify before planning:

```text
$speckit-clarify
```

6. Plan with concrete technical constraints:

```text
$speckit-plan <tech stack, architecture constraints, storage choices, testing approach>
```

7. Generate tasks and analyze consistency:

```text
$speckit-tasks
$speckit-analyze
```

8. Implement through Superpowers discipline:

- Use brainstorming or clarify if the spec is still ambiguous.
- Use TDD for behavior changes.
- Use systematic debugging for bugs.
- Use requesting-code-review and verification-before-completion before claiming completion.

9. Reconcile:

- Check `git status --short`.
- Check diffs against `spec.md`, `plan.md`, and `tasks.md`.
- Mark tasks only when there is implementation and verification evidence.
- Update Spec Kit artifacts if accepted requirements changed.

## Codex Direct Mode

When running directly in Codex:

- Prefer Spec Kit skills for artifact generation and analysis.
- Prefer Superpowers skills for execution discipline.
- Read only the active feature artifacts needed for the task; do not load every historical spec.
- Do not use `$speckit-implement` blindly if Superpowers gives a stricter TDD/review workflow for the repo. It is acceptable to execute `tasks.md` manually with Superpowers as long as the tasks and verification stay aligned.

Before editing, build a compact task context:

```text
Active feature: specs/NNN-name
Governance: .specify/memory/constitution.md
Inputs: spec.md, plan.md, tasks.md, relevant contracts/checklists
Current git status: <git status --short>
Method: Superpowers TDD/debugging/review/verification as applicable
```

## Hermes Orchestration Mode

When Hermes is the front agent, Hermes should own the conversation and use Codex only as an implementation worker.

Use Hermes `codex-delegate` when the task is large, multi-file, debugging-heavy, or explicitly requests Codex. Do not bypass `codex-delegate` with an ad hoc Codex command unless the user asked for a different launch path.

Hermes preflight:

1. Identify the target repo.
2. Read `git status --short`.
3. Locate `.specify/memory/constitution.md` and the active `specs/NNN-*` directory.
4. Decide whether the next step is Spec Kit artifact work or implementation.
5. If delegating, create a Codex task packet with the active artifacts and concise Superpowers method requirements.

Read `references/hermes-codex-delegate-spec-kit.md` when constructing a Hermes-to-Codex delegation prompt.

Hermes must verify Codex results itself:

- Read the Codex run artifacts from the run directory.
- Inspect `git status`, `git diff --stat`, and targeted diffs.
- Rerun or confirm verification evidence.
- Ensure no run artifacts entered the repo.
- Report changed files, verification commands, and remaining risks.

Codex final text is not proof. Treat it as an untrusted report until repo evidence confirms it.

## Delegation Packet Requirements

Every Hermes-to-Codex Spec Kit packet must include:

- Absolute repo path.
- Active feature path under `specs/`.
- `git status --short` before Codex starts.
- Relevant excerpts or paths for `constitution.md`, `spec.md`, `plan.md`, `tasks.md`, and checklists.
- The exact task slice Codex should implement.
- Method requirements from Superpowers, not entire skill bodies.
- Verification commands Codex may run.
- Final response format.
- A rule that Hermes owns final acceptance and any board/task lifecycle.

Use paths when files are present in the repo. Paste excerpts only for short, decisive constraints.

## Common Pitfalls

1. Using Spec Kit for every tiny edit. Use it when durable requirements and traceability pay for the overhead.
2. Treating Superpowers and Spec Kit as duplicates. They solve different problems.
3. Letting Codex implement from a chat prompt while ignoring `.specify/`.
4. Marking `tasks.md` complete because Codex said so. Require diff and verification evidence.
5. Updating code after requirements change but leaving `spec.md` stale.
6. Delegating from Hermes without passing `constitution.md`, `spec.md`, `plan.md`, and `tasks.md`.
7. Installing community Spec Kit extensions without reading the source. Extensions can write files.
8. Running Codex in a shared dirty worktree from Hermes. Use the existing `codex-delegate` isolation pattern.

## Verification Checklist

- [ ] `specify version` works.
- [ ] The target repo is initialized with `--integration codex --integration-options="--skills"` when Spec Kit is intended.
- [ ] `.specify/memory/constitution.md` exists or the user intentionally skipped constitution setup.
- [ ] Active feature has `spec.md`, `plan.md`, and `tasks.md` before implementation.
- [ ] `$speckit-analyze` or an equivalent consistency pass was run before broad implementation.
- [ ] Superpowers method requirements were applied during implementation.
- [ ] Hermes delegation used `codex-delegate` and passed Spec Kit artifacts when Hermes launched Codex.
- [ ] Final status is backed by git diff and verification evidence.
