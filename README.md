# Spec Kit Superpowers Bridge

This community-authored Codex skill connects [GitHub Spec Kit](https://github.com/github/spec-kit), [Superpowers](https://github.com/obra/superpowers), Codex, and conditional Hermes delegation. It is an independent integration, not an official release of any upstream project.

## Prerequisites

Install and configure the components separately:

- Codex with local skill support; see the official [Codex skills documentation](https://developers.openai.com/codex/skills/).
- GitHub Spec Kit and its `specify` CLI. The bridge uses project-local `.specify/` artifacts when the project has them.
- Superpowers, so its engineering-method skills are available to the same workflow.
- Hermes only when using its `codex-delegate` orchestration path; Codex direct mode does not require Hermes.

## Install

After this repository has been published, use Codex's GitHub skill installer with the repository owner substituted for `<GITHUB_OWNER>`:

```powershell
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py `
  --repo <GITHUB_OWNER>/spec-kit-superpowers-bridge-public `
  --path spec-kit-superpowers-bridge
```

Restart Codex if the installed skill does not appear. Invoke it as `$spec-kit-superpowers-bridge`, or let Codex select it when the request matches its description.

## Safe updates and rollback

The installer intentionally refuses to overwrite an existing skill. Before updating, back up the installed `spec-kit-superpowers-bridge` directory, install the new revision, and verify it. To roll back, remove the new installed directory and restore that backup directory. Do not overwrite the only known-good copy in place.

## Scope

The payload preserves the established bridge workflow: Spec Kit is the durable planning layer, Superpowers supplies engineering discipline, Codex performs repository work, and Hermes remains an optional orchestration boundary. Review the skill and all upstream dependencies before using them in a project.
