#!/usr/bin/env python3
"""Verify outputs/history.json against the committee PDFs.

Usage: verify_history.py HISTORY_JSON COMMITTEE_DIR

Checks: JSON shape; every item (anywhere in the tree) that has a `source`
also has an integer `pdf_page`; the source file exists; every `quote` is
found on the stated page after normalisation (whitespace ignored, bullet
glyphs and page footers ignored, quote/dash glyphs unified).
Exit 0 with ALL CHECKS PASSED when clean.  Reads each PDF with every available
extractor (pypdf, plus `pdftotext` plain and -layout when on PATH); a quote is
found when any of them has it on the page, since they differ in word spacing
and table reading order.
"""
import json, re, shutil, subprocess, sys
from pathlib import Path

TOP = ("generated_at", "source_documents", "gaps", "audits", "opinion_basis", "agreed_actions",
       "planned_audits", "audit_approach", "risk_themes", "scoring_method", "discrepancies")
GLYPHS = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"',
                        "–": "-", "\u2014": "-", " ": " "})
BULLET_RE = re.compile(r"[-•▪●⁃…]")


def normalise(t: str) -> str:
    t = t.translate(GLYPHS)
    t = BULLET_RE.sub(" ", t)
    return re.sub(r"\s+", " ", t).strip()


def compact(t: str) -> str:
    return normalise(t).replace(" ", "")


def pages(pdf: Path) -> list[list[str]]:
    """One list of whitespace-free page texts per available extractor."""
    renderings = []
    try:
        from pypdf import PdfReader
        renderings.append([p.extract_text() or "" for p in PdfReader(pdf).pages])
    except ImportError:
        pass
    if shutil.which("pdftotext"):
        for flags in ([], ["-layout"]):
            out = subprocess.run(["pdftotext", *flags, str(pdf), "-"], capture_output=True, text=True, check=True).stdout
            ps = out.split("\f")
            if ps and not ps[-1].strip():
                ps.pop()
            renderings.append(ps)
    if not renderings:
        sys.exit("ERROR: need pdftotext on PATH or the pypdf package installed")
    return [[compact(p) for p in r] for r in renderings]


def on_page(quote: str, renderings: list[list[str]], page: int) -> bool:
    return any(page <= len(r) and quote in r[page - 1] for r in renderings)


def walk(node, path="$"):
    """Yield (path, dict) for every dict in the tree."""
    if isinstance(node, dict):
        yield path, node
        for k, v in node.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, f"{path}[{i}]")


def main(hist: str, cdir: str) -> int:
    errors, warnings = [], []
    try:
        doc = json.loads(Path(hist).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR: cannot read {hist}: {e}")
        return 1
    for k in TOP:
        if k not in doc:
            errors.append(f"top-level key missing: {k}")
    cache: dict[str, list[list[str]]] = {}
    n_items = n_quotes = 0
    for path, d in walk(doc):
        src = d.get("source")
        if src is None:
            if "quote" in d:
                errors.append(f"{path}: has a quote but no source")
            continue
        n_items += 1
        f = Path(cdir) / src
        if not f.exists():
            errors.append(f"{path}: source file not found: {src}")
            continue
        page = d.get("pdf_page")
        if not isinstance(page, int) or isinstance(page, bool):
            errors.append(f"{path}: pdf_page missing or not an integer")
            continue
        if src not in cache:
            cache[src] = pages(f)
        rs = cache[src]
        n_pages = max(len(r) for r in rs)
        if not 1 <= page <= n_pages:
            errors.append(f"{path}: pdf_page {page} out of range 1..{n_pages} for {src}")
            continue
        q = d.get("quote")
        if q is None:
            continue
        n_quotes += 1
        nq = compact(str(q))
        if len(normalise(str(q))) < 12:
            errors.append(f"{path}: quote too short ({len(normalise(str(q)))} chars)")
        elif on_page(nq, rs, page):
            pass
        else:
            hits = [n for n in range(1, n_pages + 1) if on_page(nq, rs, n)]
            if hits:
                errors.append(f"{path}: quote is on page(s) {hits}, not pdf_page {page}: {q[:60]!r}…")
            elif any(nq in "".join(r) for r in rs):
                errors.append(f"{path}: quote straddles a page boundary: {q[:60]!r}…")
            else:
                errors.append(f"{path}: quote NOT FOUND in {src}: {q[:60]!r}…")
    sm = doc.get("scoring_method", {})
    if isinstance(sm, dict) and "usable" not in sm:
        errors.append("scoring_method.usable missing")
    print(f"history.json: {n_items} sourced items, {n_quotes} quotes, {len(cache)} documents")
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("FAIL ", e)
    if errors:
        print(f"\n{len(errors)} failure(s)")
        return 1
    print("\nALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
