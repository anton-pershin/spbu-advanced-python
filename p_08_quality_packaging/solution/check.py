"""Quality gate for logtools package.

Run from repo root:
    python -m p_08_quality_packaging.solution.check

This script runs:
    - pytest (tests)
    - black --check (formatting)
    - isort --check-only (imports)
    - mypy (type checking)
    - pylint (linting)
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], cwd: Path) -> bool:
    """Run command and return True if successful."""
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FAILED: {' '.join(cmd)}")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return False
    return True


def main() -> int:
    """Run all quality checks."""
    cwd = Path(__file__).parent

    checks = [
        ([sys.executable, "-m", "pytest", "tests"], "pytest"),
        ([sys.executable, "-m", "black", "--check", "src", "tests"], "black"),
        ([sys.executable, "-m", "isort", "--check-only", "src", "tests"], "isort"),
        ([sys.executable, "-m", "mypy", "src"], "mypy"),
        ([sys.executable, "-m", "pylint", "src/logtools"], "pylint"),
    ]

    all_passed = True
    for cmd, name in checks:
        if not run_command(cmd, cwd):
            all_passed = False
        else:
            print(f"OK: {name}")

    if all_passed:
        print("\nAll checks passed!")
        return 0
    else:
        print("\nSome checks failed.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
