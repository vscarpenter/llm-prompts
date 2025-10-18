#!/usr/bin/env python3
"""Fix leading '+' characters in markdown prompt files.

This script walks the `prompts/` directory and for each .md file:
- creates a .bak backup of the original file
- removes leading '+' characters at the start of lines (including '+-' and '+```')
- writes the cleaned content back to the file

Run this from the repo root with Python 3.
"""
import os
import re
from pathlib import Path


def clean_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not re.search(r"(?m)^\+", text):
        return False

    backup = path.with_suffix(path.suffix + ".bak")
    backup.write_text(text, encoding="utf-8")

    # Remove a single leading plus and an optional following space on each line
    cleaned = re.sub(r"(?m)^\+\s?", "", text)

    path.write_text(cleaned, encoding="utf-8")
    return True


def main():
    repo_root = Path(__file__).resolve().parents[1]
    prompts_dir = repo_root / "prompts"
    changed = []

    for root, dirs, files in os.walk(prompts_dir):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = Path(root) / fname
            try:
                if clean_file(fpath):
                    changed.append(str(fpath.relative_to(repo_root)))
            except Exception as e:
                print(f"ERROR processing {fpath}: {e}")

    if changed:
        print("Cleaned files:")
        for p in changed:
            print(" -", p)
    else:
        print("No files needed cleaning.")


if __name__ == "__main__":
    main()
