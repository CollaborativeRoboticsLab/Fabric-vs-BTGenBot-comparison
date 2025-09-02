from __future__ import annotations

import re
import csv
from pathlib import Path
from typing import Dict, List, Tuple

# -----------------------------
# Inputs & model mapping
# -----------------------------

LOG_FILES = [
    "codellama-rawlog.log",
    "llamachat-rawlog.log",
    "openai-4.1-rawlog.log",
    "openai-4o-rawlog.log",
    "openai-5-rawlog.log",
]

MODEL_NAME_MAP = {
    "codellama-rawlog.log": "codellama",
    "llamachat-rawlog.log": "llamachat",
    "openai-4.1-rawlog.log": "gpt-4.1",
    "openai-4o-rawlog.log": "gpt-4o",
    "openai-5-rawlog.log": "gpt-5",
}

IS_GPT = {
    "codellama-rawlog.log": False,
    "llamachat-rawlog.log": False,
    "openai-4.1-rawlog.log": True,
    "openai-4o-rawlog.log": True,
    "openai-5-rawlog.log": True,
}

# Labels present in logs
MODEL_LABELS: Tuple[str, ...] = (
    "Zero-shot base model result",
    "One-shot base model result",
    "Zero-shot finetuned model result",
    "One-shot finetuned model result",
)

# Map labels to (version, prompt)
LABEL_TO_VERSION_PROMPT = {
    "Zero-shot base model result": ("base", "zero"),
    "One-shot base model result": ("base", "one"),
    "Zero-shot finetuned model result": ("finetuned", "zero"),
    "One-shot finetuned model result": ("finetuned", "one"),
}

# -----------------------------
# Regex
# -----------------------------

ITERATION_RE = re.compile(r"(?m)^\s*Iteration\s+(\d+)\s*:\s*$")
RESULT_LINE_RE = re.compile(
    r"^(?:"
    + "|".join(map(re.escape, MODEL_LABELS))
    + r")\s*\(time:\s*([\d.]+)\s*seconds\):\s*$"
)

# -----------------------------
# File IO helpers
# -----------------------------

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")

def write_csv(path: Path, rows: List[List[str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)

# -----------------------------
# Parsing / extraction
# -----------------------------

def extract_blocks(log_text: str) -> Dict[int, List[str]]:
    blocks: Dict[int, List[str]] = {}
    current_it: int | None = None

    for raw in log_text.splitlines():
        line = raw.rstrip()

        m_it = ITERATION_RE.match(line)
        if m_it:
            current_it = int(m_it.group(1))
            blocks[current_it] = [f"Iteration {current_it}:"]
            continue

        if current_it is not None and any(line.startswith(lbl) for lbl in MODEL_LABELS):
            blocks[current_it].append(line)

    return {k: v for k, v in blocks.items() if 1 <= k <= 10}

def parse_times(blocks: Dict[int, List[str]]) -> Dict[str, Dict[int, float]]:
    results: Dict[str, Dict[int, float]] = {lbl: {} for lbl in MODEL_LABELS}
    for it, lines in blocks.items():
        for line in lines:
            m = RESULT_LINE_RE.match(line)
            if m:
                label = next((lbl for lbl in MODEL_LABELS if line.startswith(lbl)), None)
                if label:
                    results[label][it] = float(m.group(1))
    return results

# -----------------------------
# Formatting for outputs
# -----------------------------

def format_blocks_as_text(blocks: Dict[int, List[str]]) -> str:
    parts: List[str] = []
    for it in sorted(blocks):
        parts.append("\n".join(blocks[it]))
    return "\n\n".join(parts) + ("\n" if parts else "")

def make_iteration_headers(all_iterations: List[int]) -> List[str]:
    return [f"Itr{it}" for it in all_iterations]

# -----------------------------
# Row building (combined CSV)
# -----------------------------

def rows_for_file(
    file_name: str,
    times_by_label: Dict[str, Dict[int, float]],
    all_iterations: List[int]
) -> List[List[str]]:
    model = MODEL_NAME_MAP[file_name]
    is_gpt = IS_GPT[file_name]
    rows: List[List[str]] = []

    for label in MODEL_LABELS:
        version, prompt = LABEL_TO_VERSION_PROMPT[label]
        version_out = "n/a" if is_gpt else version

        row = [model, version_out, prompt]
        for it in all_iterations:
            val = times_by_label.get(label, {}).get(it, "")
            row.append(f"{val}" if val != "" else "")
        rows.append(row)

    return rows

# -----------------------------
# Orchestration
# -----------------------------

def process_one_log(file_name: str) -> Tuple[Dict[str, Dict[int, float]], Dict[int, List[str]]]:
    p = Path(file_name)
    if not p.exists():
        return ({lbl: {} for lbl in MODEL_LABELS}, {})

    text = read_text(p)
    blocks = extract_blocks(text)
    times = parse_times(blocks)
    return (times, blocks)

def main() -> None:
    out_dir = Path("timing_data")
    out_dir.mkdir(exist_ok=True)

    per_file_times: Dict[str, Dict[str, Dict[int, float]]] = {}
    per_file_blocks: Dict[str, Dict[int, List[str]]] = {}

    for fname in LOG_FILES:
        times, blocks = process_one_log(fname)
        per_file_times[fname] = times
        per_file_blocks[fname] = blocks

        # Write per-file extracted text to timing_data/
        out_txt = out_dir / (Path(fname).stem + ".extracted.txt")
        write_text(out_txt, format_blocks_as_text(blocks))

    # Collect all iteration indices across files to form CSV headers
    all_iterations_sorted = sorted({
        it for blocks in per_file_blocks.values() for it in blocks.keys()
    })

    header = ["Model", "Version", "Prompt"] + make_iteration_headers(all_iterations_sorted)
    rows: List[List[str]] = [header]

    for fname in LOG_FILES:
        rows.extend(rows_for_file(fname, per_file_times[fname], all_iterations_sorted))

    # Write combined CSV to timing_data/
    write_csv(out_dir / "iteration_times_all.csv", rows)

if __name__ == "__main__":
    main()
