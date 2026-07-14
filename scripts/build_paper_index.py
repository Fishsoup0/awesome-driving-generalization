#!/usr/bin/env python3
"""Build the human-readable paper index from data/papers.csv."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "papers.csv"
OUTPUT = ROOT / "papers" / "README.md"

GROUPS = [
    "Data, simulation, reconstruction, and generation",
    "Open-world and foundation representations",
    "Domain generalization, adaptation, and robust training",
    "Evaluation, uncertainty, and safety",
    "Predictive world models and end-to-end driving",
]


def group_for(row: dict[str, str]) -> str:
    category = row["category"].casefold()
    title = row["title"].casefold()
    if any(token in category for token in ("world model", "end-to-end")):
        return GROUPS[4]
    if any(token in category for token in ("generation", "simulation", "reconstruction")):
        return GROUPS[0]
    if any(token in category for token in ("open-world", "foundation", "open-vocabulary")):
        return GROUPS[1]
    if any(token in category for token in ("adaptation", "generalization", "training", "causal", "robust restoration", "robust collaborative")):
        return GROUPS[2]
    if any(token in category for token in ("benchmark", "evaluation", "uncertainty", "safety", "dataset")):
        return GROUPS[3]
    if any(token in title for token in ("benchmark", "dataset", "uncertainty")):
        return GROUPS[3]
    return GROUPS[2]


def escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def main() -> None:
    with CATALOG.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    rows.sort(key=lambda row: (-int(row["year"]), row["title"].casefold()))
    years = Counter(row["year"] for row in rows)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[group_for(row)].append(row)

    lines = [
        "# Curated paper library",
        "",
        f"**{len(rows)} papers** spanning driving-specific generalization, adaptation, robustness, open-world perception, simulation, evaluation, and world models. The catalog emphasizes 2023–2026 top-venue work while retaining essential foundations.",
        "",
        "The canonical metadata is [`../data/papers.csv`](../data/papers.csv). This page is generated from that file with `python scripts/build_paper_index.py`.",
        "",
        "## Coverage at a glance",
        "",
        "| Year | Papers |",
        "|---:|---:|",
    ]
    for year, count in sorted(years.items(), reverse=True):
        lines.append(f"| {year} | {count} |")

    for group in GROUPS:
        items = grouped[group]
        lines.extend([
            "",
            f"## {group} ({len(items)})",
            "",
            "| Year | Paper | Venue | Modality | Shift / focus | Code |",
            "|---:|---|---:|---|---|---|",
        ])
        for row in items:
            paper = f"[{escape(row['title'])}]({row['paper_url']})"
            code = f"[code]({row['code_url']})" if row["code_url"] else "—"
            lines.append(
                f"| {row['year']} | {paper} | {escape(row['venue'])} | "
                f"{escape(row['modality'])} | {escape(row['shift_or_focus'])} | {code} |"
            )

    lines.extend([
        "",
        "## Inclusion checklist",
        "",
        "A new entry should state the distribution shift or long-tail failure, the sensor/task assumptions, the source/target supervision available, and the evaluation protocol. Prefer official proceedings, arXiv records, and author-maintained code repositories.",
        "",
    ])
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
