#!/usr/bin/env python3
"""Public mirror hygiene checks for AgentResponsibilityEngineering."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "NOTICE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CITATION.cff",
    "docs/public-boundary.md",
    "docs/validation-tiers.md",
    "docs/stamp-paper/EVIDENCE_PUBLIC_SUMMARY.md",
    "research/stpa/STPA_RESOLUTION.md",
]

SKIP_DIRS = {".git", "__pycache__"}
TEXT_SUFFIXES = {".md", ".txt", ".cff", ".yml", ".yaml", ".py"}
BINARY_SUFFIXES = {".pdf", ".docx", ".png", ".jpg", ".jpeg", ".gif"}

SECRET_PATTERNS = [
    re.compile(r"sk_[A-Za-z0-9]{20,}"),
    re.compile(r"cfat_[A-Za-z0-9]{20,}"),
    re.compile(r"(?i)bearer\s+(?!<token>)[A-Za-z0-9._\-]{24,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)?PRIVATE KEY-----"),
    re.compile(r"(?i)(api[_-]?key|client[_-]?secret|password)\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
]

LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.is_file():
            files.append(path)
    return files


def is_text(path: Path) -> bool:
    if path.suffix.lower() in BINARY_SUFFIXES:
        return False
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in REQUIRED_FILES


def check_required() -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")
    return errors


def normalize_link_target(raw: str) -> str:
    target = raw.strip().split("#", 1)[0]
    target = target.split("?", 1)[0]
    return unquote(target)


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in LINK_PATTERN.finditer(text):
            raw_target = match.group(1).strip()
            if raw_target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = normalize_link_target(raw_target)
            if not target:
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)} links outside repo: {raw_target}")
                continue
            if not candidate.exists():
                errors.append(f"{path.relative_to(ROOT)} has broken link: {raw_target}")
    return errors


def check_secret_shapes() -> list[str]:
    errors: list[str] = []
    for path in iter_files():
        if not is_text(path):
            continue
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"{rel} contains secret-shaped text matching {pattern.pattern}")
    return errors


def main() -> int:
    errors = []
    errors.extend(check_required())
    errors.extend(check_markdown_links())
    errors.extend(check_secret_shapes())

    if errors:
        print("PUBLIC REPO AUDIT: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PUBLIC REPO AUDIT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
