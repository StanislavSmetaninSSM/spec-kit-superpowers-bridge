#!/usr/bin/env python3
"""Install the bridge as repository-local Arena instructions. No external dependencies."""
import argparse
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent.parent / 'spec-kit-superpowers-bridge'
START = '<!-- spec-kit-superpowers-bridge:arena:start -->'
END = '<!-- spec-kit-superpowers-bridge:arena:end -->'
BLOCK = f'''{START}
## Spec Kit Superpowers Bridge (Arena)

When a task involves Spec Kit, Superpowers, `.specify/`, or a durable feature workflow, read `.agents/skills/spec-kit-superpowers-bridge/SKILL.md` and its `references/arena.md` before proceeding. Follow the Arena adaptation and all higher-priority instructions.
{END}'''


def same_tree(source, target):
    if not target.is_dir() or target.is_symlink():
        return False
    files = [p for p in source.rglob('*') if p.is_file()]
    return all((target / p.relative_to(source)).is_file() and
               not (target / p.relative_to(source)).is_symlink() and
               p.read_bytes() == (target / p.relative_to(source)).read_bytes() for p in files)


def install(repo):
    repo = repo.resolve()
    if not repo.is_dir() or not (repo / '.git').exists():
        raise ValueError(f'Not a Git working tree root: {repo}')
    target = repo / '.agents' / 'skills' / 'spec-kit-superpowers-bridge'
    agents = repo / 'AGENTS.md'
    if any(p.is_symlink() for p in (repo / '.agents', repo / '.agents' / 'skills', target, agents)):
        raise ValueError('Refusing to install through a symlink in the destination path.')
    if target.exists() and not same_tree(SOURCE, target):
        raise ValueError(f'Existing skill differs; review it before updating: {target}')
    text = agents.read_text(encoding='utf-8') if agents.exists() else ''
    if START in text or END in text:
        if text.count(START) != 1 or text.count(END) != 1 or text.index(START) > text.index(END):
            raise ValueError('AGENTS.md contains malformed bridge markers; resolve them manually.')
        current = text[text.index(START):text.index(END) + len(END)]
        if current != BLOCK:
            raise ValueError('Existing Arena instructions differ; review them before updating AGENTS.md.')
        updated = text
    else:
        updated = text + ('\n' if text and not text.endswith('\n') else '') + ('\n' if text else '') + BLOCK + '\n'
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SOURCE, target)
    if updated != text:
        agents.write_text(updated, encoding='utf-8')
    print(f'Arena bridge installed in {repo}. Review AGENTS.md and .agents/skills; commit them if desired.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repository', type=Path, help='Path to the target Git working tree root')
    args = parser.parse_args()
    try:
        install(args.repository)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f'Installation stopped: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
