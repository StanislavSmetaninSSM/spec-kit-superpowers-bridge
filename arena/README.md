# Arena Agent Mode adaptation

Use this optional guidance when executing the shared bridge in Arena. The shared skill is application-independent; this document supplies Arena-specific operating guidance. Platform, developer, user, and repository instructions take precedence, including branch, worktree, installation, network, and safety restrictions. The Arena installer copies this document to the installed skill's `references/arena.md` for compatibility with its marked `AGENTS.md` instruction.

## Setup and capability checks

- Read the target repository's `AGENTS.md`, inspect `git status --short`, and preserve unrelated changes. Work on the branch assigned by Arena; do not create branches or worktrees when prohibited.
- Inspect `.specify/`, `specs/`, available tools, and project instructions. Do not assume `$speckit-*`, Superpowers skills, Codex, Hermes, PowerShell, `uv`, or `specify` are installed. Do not invoke a skill or delegation tool that is unavailable.
- Installation of this bridge is not permission to install other software, initialize Spec Kit, create specifications, or overwrite project files. Initialize or add scaffolding only within existing user authorization. For existing project scaffolding, follow its instructions; use native commands only if available and applicable. Do not select another application's integration as an Arena default.
- If skill invocation is unavailable but instructions are accessible, read them and identify the fallback honestly. If a required capability is missing, identify the unmet check and continue only independent authorized work. Applying relevant principles directly does not establish that the missing phase, command, or independent review ran. Optional dependencies do not block work that does not require them.

## Feature workflow

Locate the active feature and read only its relevant constitution, spec, plan, tasks, and contracts. Apply the shared skill's phase mapping and evidence rules within higher-priority instructions. Brainstorming under the shared workflow requires Spec Kit even for tiny, bounded, or investigative work. Scale the artifacts to the task. Ordinary questions do not start development. Use available Spec Kit tooling if the project provides it; identify an equivalent consistency check honestly when applicable. Do not fabricate missing artifacts or mark tasks complete without evidence. Resolve material ambiguity with the user; preserve concrete prior approvals and use reasonable assumptions within approved scope.

Implement directly using the tools available in Arena. Load and apply the relevant Superpowers instructions, including TDD for behavior changes, systematic debugging for defects, separate independent review, and verification before completion. Respect the assigned branch; delegation requires actual capability and applicable authorization. Inspect the diff against the approved requirements and report the changes, tests and their results, any unverified items, and spec drift. A missing independent reviewer remains an unmet check rather than a self-review presented as independent.
