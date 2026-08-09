# Spec Kit Superpowers Bridge

This community-authored Codex skill connects [GitHub Spec Kit](https://github.com/github/spec-kit), [Superpowers](https://github.com/obra/superpowers), Codex, and conditional Hermes delegation. It is an independent integration, not an official release of any upstream project.

## Prerequisites

Install and configure the components separately:

- Codex with local skill support; see the official [Codex skills documentation](https://developers.openai.com/codex/skills/).
- GitHub Spec Kit and its `specify` CLI. The bridge uses project-local `.specify/` artifacts when the project has them.
- Superpowers, so its engineering-method skills are available to the same workflow.
- Hermes only when using its `codex-delegate` orchestration path; Codex direct mode does not require Hermes.

## Install

Install from the published bridge repository:

```powershell
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py `
  --repo StanislavSmetaninSSM/spec-kit-superpowers-bridge `
  --path spec-kit-superpowers-bridge
```

Restart Codex if the installed skill does not appear. Invoke it as `$spec-kit-superpowers-bridge`, or let Codex select it when the request matches its description.

Published source: <https://github.com/StanislavSmetaninSSM/spec-kit-superpowers-bridge>

## Safe updates and rollback

The installer intentionally refuses to overwrite an existing skill. Use this fail-fast PowerShell procedure to download and validate a replacement before touching the current installation. It leaves the unique backup in place after success so you can roll back deliberately.

```powershell
$ErrorActionPreference = 'Stop'
$skillName = 'spec-kit-superpowers-bridge'
$repository = 'StanislavSmetaninSSM/spec-kit-superpowers-bridge'
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$skillsRoot = Join-Path $codexHome 'skills'
$installer = Join-Path $skillsRoot '.system/skill-installer/scripts/install-skill-from-github.py'
$validator = Join-Path $skillsRoot '.system/skill-creator/scripts/quick_validate.py'
$python = (Get-Command python -ErrorAction Stop).Source
$target = Join-Path $skillsRoot $skillName
$stagingRoot = Join-Path ([System.IO.Path]::GetTempPath()) "$skillName-stage-$([guid]::NewGuid().ToString('N'))"
$stagedSkill = Join-Path $stagingRoot $skillName
$backup = "$target.backup-$([guid]::NewGuid().ToString('N'))"
$hadTarget = Test-Path -LiteralPath $target
$backupCreated = $false

if (-not (Test-Path -LiteralPath $installer -PathType Leaf)) { throw "Codex installer not found: $installer" }
if (-not (Test-Path -LiteralPath $validator -PathType Leaf)) { throw "Codex validator not found: $validator" }
New-Item -ItemType Directory -LiteralPath $stagingRoot -ErrorAction Stop | Out-Null

try {
  # The current install remains untouched through download and staged validation.
  & $python $installer --repo $repository --path $skillName --dest $stagingRoot
  if ($LASTEXITCODE -ne 0) { throw "Installer failed with exit code $LASTEXITCODE" }
  & $python $validator $stagedSkill
  if ($LASTEXITCODE -ne 0) { throw "Staged validation failed with exit code $LASTEXITCODE" }

  if ($hadTarget) {
    Move-Item -LiteralPath $target -Destination $backup -ErrorAction Stop
    $backupCreated = $true
  }
  Move-Item -LiteralPath $stagedSkill -Destination $target -ErrorAction Stop
  & $python $validator $target
  if ($LASTEXITCODE -ne 0) { throw "Final validation failed with exit code $LASTEXITCODE" }
  if ($backupCreated) {
    Write-Host "Updated $target. Rollback copy retained at $backup"
  } else {
    Write-Host "Fresh installation complete; no previous copy existed at $target"
  }
}
catch {
  # Roll back every unsuccessful swap or final-validation failure.
  if ($backupCreated -and (Test-Path -LiteralPath $target)) {
    Remove-Item -LiteralPath $target -Recurse -Force -ErrorAction SilentlyContinue
  }
  if ($backupCreated -and (Test-Path -LiteralPath $backup)) {
    Move-Item -LiteralPath $backup -Destination $target -ErrorAction Stop
  } elseif (-not $hadTarget -and (Test-Path -LiteralPath $target)) {
    # A fresh install has no previous copy; only its partial replacement may be removed.
    Remove-Item -LiteralPath $target -Recurse -Force -ErrorAction SilentlyContinue
  }
  if ($hadTarget -and -not $backupCreated -and (Test-Path -LiteralPath $target)) {
    # The backup move failed, so the original installation remains intact.
    Write-Warning "Update stopped before backup; original installation remains at $target"
  }
  throw
}
finally {
  if (Test-Path -LiteralPath $stagingRoot) {
    Remove-Item -LiteralPath $stagingRoot -Recurse -Force -ErrorAction SilentlyContinue
  }
}
```

To roll back a successful update later, remove the updated target only after confirming the unique backup still exists, then move that backup directory back to the target path and run `quick_validate.py` on the restored target.

## Scope

The payload preserves the established bridge workflow: Spec Kit is the durable planning layer, Superpowers supplies engineering discipline, Codex performs repository work, and Hermes remains an optional orchestration boundary. Review the skill and all upstream dependencies before using them in a project.
