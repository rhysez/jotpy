#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import pytest

def main():
    # Project root
    project_root = Path(__file__).resolve().parent.parent

    # Add src/ to sys.path so tests can import classes
    src_path = project_root / "src"
    sys.path.insert(0, str(src_path))

    # Run pytest on the tests folder
    tests_path = project_root / "tests"
    print(f"Running pytest with src in sys.path: {src_path}")
    exit_code = pytest.main([str(tests_path)])

    sys.exit(exit_code)

if __name__ == "__main__":
    main()


