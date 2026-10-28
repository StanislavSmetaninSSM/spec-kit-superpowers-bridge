# Arena Agent Mode adaptation

Use this guidance when executing this bridge in Arena. Arena is the direct implementation agent, not Codex or Hermes. The main skill's Codex and Hermes commands are examples for those environments, not prerequisites or commands to execute in Arena. Platform, developer, user, and repository instructions take precedence over this skill, including branch, worktree, installation, network, and safety restrictions.

## Setup and capability checks

- Read the target repository's `AGENTS.md`, inspect `git status --short`, and preserve unrelated changes. Work on the branch assigned by Arena; do not create branches or worktrees when prohibited.
- Inspect `.specify/`, `specs/`, available tools, and project instructions. Do not assume `$speckit-*`, Superpowers skills, Codex, Hermes, PowerShell, `uv`, or `specify` are installed. Do not invoke a skill or delegation tool that is unavailable.
- Installation of this bridge is not permission to install other software, initialize Spec Kit, create specifications, or overwrite project files. Only initialize or add scaffolding when the user has approved it. For existing project scaffolding, follow its instructions; use native commands only if available and applicable. Avoid running `specify init` with a Codex integration merely because the main skill shows it.
- If Spec Kit or Superpowers is absent, apply their relevant principles directly: inspect existing requirements, plan proportionately, use tests and systematic debugging, review the diff, and verify. Clearly distinguish this from actually running an unavailable skill or command. Do not block ordinary implementation on optional dependencies.

## Feature workflow

For work that warrants durable specs, locate the active feature and read only its relevant constitution, spec, plan, tasks, and contracts. Follow the main skill's source-of-truth and reconciliation rules within higher-priority instructions. Use available Spec Kit tooling if the project provides it; otherwise review consistency manually. Do not fabricate missing artifacts or mark tasks complete without evidence. Resolve material ambiguity with the user; use reasonable assumptions where permitted rather than asking unnecessary questions.

Implement directly using the tools available in Arena. Apply TDD where practical, systematic debugging to defects, focused review, and verification before completion. Respect the assigned branch; do not delegate to Codex or Hermes unless explicitly requested and actually available. Inspect the diff and report the changes, tests and their results, any unverified items, and spec drift. For small changes, avoid unnecessary planning scaffolding.
