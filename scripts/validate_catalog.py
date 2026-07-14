#!/usr/bin/env python3
"""Validate required fields and basic consistency in the research catalogs."""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CATALOGS = {
    ROOT / "data" / "papers.csv": {
        "year", "title", "venue", "category", "modality", "shift_or_focus", "paper_url", "code_url"
    },
    ROOT / "data" / "datasets.csv": {
        "year", "dataset", "type", "modalities", "conditions_or_scale", "tasks", "generalization_axis", "paper_or_project_url"
    },
}


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate(path: Path, required: set[str]) -> list[str]:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = required - set(reader.fieldnames or [])
        if missing:
            return [f"{path}: missing columns {sorted(missing)}"]

        seen: set[str] = set()
        for line, row in enumerate(reader, start=2):
            key = (row.get("title") or row.get("dataset") or "").strip().casefold()
            if not key:
                errors.append(f"{path}:{line}: empty title/dataset")
            elif key in seen:
                errors.append(f"{path}:{line}: duplicate entry {key!r}")
            seen.add(key)

            year = row.get("year", "")
            if not (year.isdigit() and 2000 <= int(year) <= 2030):
                errors.append(f"{path}:{line}: invalid year {year!r}")

            for column, value in row.items():
                if column.endswith("_url") and value and not valid_url(value):
                    errors.append(f"{path}:{line}: invalid HTTPS URL in {column}")
    return errors


def main() -> int:
    errors = [error for path, fields in CATALOGS.items() for error in validate(path, fields)]
    if errors:
        print("Catalog validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Validated {len(CATALOGS)} catalogs successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
