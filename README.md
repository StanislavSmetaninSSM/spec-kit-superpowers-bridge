# Spec Kit Superpowers Bridge

This community-authored skill connects [GitHub Spec Kit](https://github.com/github/spec-kit) and [Superpowers](https://github.com/obra/superpowers). Spec Kit owns requirements, decisions, and task tracking; Superpowers supplies the engineering methods. This is an independent integration, not an official release of either upstream project.

The shared skill is application-independent. It uses the current agent's available capabilities without selecting an application, model, operating system, or delegation tool. Optional application adapters live outside the shared skill directory.

## Use the shared skill

Install and configure Spec Kit and Superpowers separately for your environment. The bridge does not install dependencies or grant permission to initialize a project, publish changes, or switch agent applications.

Review this repository, then install the `spec-kit-superpowers-bridge/` directory through your environment's supported skill mechanism, or read its [SKILL.md](spec-kit-superpowers-bridge/SKILL.md) as instructions when file-based skills are unavailable. Follow the environment's discovery and invocation rules. The optional `agents/openai.yaml` file supplies UI metadata for compatible hosts; it is not required to follow the methodology.

The bridge keeps one active feature and one canonical set of `spec.md`, `plan.md`, and `tasks.md` artifacts. It maps the actual available Spec Kit phases to applicable Superpowers skills, preserves concrete prior approvals, and requires evidence for completion. Under the workflow encoded by this skill, brainstorming requires Spec Kit even for tiny, bounded, or investigative tasks; ordinary questions do not initiate development.

Unavailable tools must be reported accurately. Reading instructions or applying equivalent practices does not establish that an unavailable skill or command ran, or that a required independent review was completed.

## Optional Arena adapter

The existing [Arena adaptation](arena/README.md) supports repository-local instructions without assuming a global skill installer. From a reviewed checkout of this repository, run with Python 3:

```bash
python3 arena/install.py /absolute/path/to/target-repository
```

The target must be the root of an existing Git working tree. The installer copies the shared skill into `.agents/skills/spec-kit-superpowers-bridge/`, adds the Arena adaptation at the existing installed path `references/arena.md`, and adds a marked instruction to `AGENTS.md`. The adapter source remains outside the shared skill. Existing instructions are preserved; identical installations are repeatable; differing installations or edited bridge blocks require manual review. Installation does not install Spec Kit, Superpowers, or another agent application.

Read the installed `SKILL.md` and `references/arena.md` after installation. Future sessions follow the repository's `AGENTS.md`. Review the resulting project changes and commit only if desired.

## Updates and removal

Back up the installed files and local changes before updating. Review a replacement checkout before replacing an existing shared skill. Use your environment's installation rules; do not assume its installer overwrites existing skills.

For an Arena installation, review and manually remove or replace the installed skill and marked `AGENTS.md` block before rerunning the installer. To uninstall, remove `.agents/skills/spec-kit-superpowers-bridge/` and only the block between `<!-- spec-kit-superpowers-bridge:arena:start -->` and `<!-- spec-kit-superpowers-bridge:arena:end -->` in `AGENTS.md`. Delete `AGENTS.md` only if otherwise empty. Restore your backup to roll back an update.

## Verification

Run the Arena installer tests from the repository root:

```bash
python3 -m unittest discover -s tests -v
```

These tests verify packaging and installation behavior. They do not establish that an agent will always follow the workflow. The shared skill can also be checked with a compatible skill validator available in your environment.

See [LICENSE](LICENSE) for licensing and upstream attribution.
