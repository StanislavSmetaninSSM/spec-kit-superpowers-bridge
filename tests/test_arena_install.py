import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / 'arena' / 'install.py'


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        (self.repo / '.git').mkdir()

    def run_install(self):
        return subprocess.run([sys.executable, str(INSTALLER), str(self.repo)], capture_output=True, text=True)

    def test_install_preserves_instructions_and_is_idempotent(self):
        agents = self.repo / 'AGENTS.md'
        agents.write_text('# Existing instructions\n', encoding='utf-8')
        self.assertEqual(self.run_install().returncode, 0)
        first = agents.read_bytes()
        self.assertIn(b'# Existing instructions', first)
        self.assertTrue((self.repo / '.agents/skills/spec-kit-superpowers-bridge/references/arena.md').is_file())
        self.assertEqual(self.run_install().returncode, 0)
        self.assertEqual(agents.read_bytes(), first)

    def test_refuses_different_existing_skill_before_touching_agents(self):
        skill = self.repo / '.agents/skills/spec-kit-superpowers-bridge'
        skill.mkdir(parents=True)
        (skill / 'SKILL.md').write_text('local changes')
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertEqual((skill / 'SKILL.md').read_text(), 'local changes')
        self.assertFalse((self.repo / 'AGENTS.md').exists())

    def test_refuses_edited_block(self):
        self.assertEqual(self.run_install().returncode, 0)
        agents = self.repo / 'AGENTS.md'
        agents.write_text(agents.read_text().replace('## Spec Kit', '## Changed Spec Kit'))
        before = agents.read_bytes()
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertEqual(agents.read_bytes(), before)

    def test_rejects_non_git_directory(self):
        (self.repo / '.git').rmdir()
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertFalse((self.repo / 'AGENTS.md').exists())


if __name__ == '__main__':
    unittest.main()
