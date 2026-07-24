#!/usr/bin/env python3
"""
build_manifest.py — regenerate manifest.json for the Argon 40 public
datasheet index (index.html) from the datasheets/ folder on disk.

Run from the repo root:

    python3 scripts/build_manifest.py

Reads, per SKU folder under datasheets/<SKU>/:
  - product.json      name, family, category, compatible_with, description, tags
                       (written by wiki_tool.py's `datasheet` command since the
                       product.json patch — see argon-wiki/wiki_tool.py)
  - version-log.json   document_version, product_revision, generated_at
  - <SKU>-datasheet.pdf   used only for file size + existence check

Writes manifest.json at the repo root. index.html fetches that file at
page load — this script is the only thing that has to run to keep the
public page in sync; it does no network calls, so it works identically
locally and inside the build-index.yml GitHub Action.

SKUs missing product.json (e.g. datasheets pushed before that file was
introduced) are still listed with placeholder metadata, and are called
out in the printed summary so they can be backfilled with:

    python3 wiki_tool.py datasheet --sku <SKU> --force
"""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATASHEETS_DIR = REPO_ROOT / "datasheets"
MANIFEST_PATH = REPO_ROOT / "manifest.json"


def load_json(path: Path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"  ⚠ could not parse {path}: {e}", file=sys.stderr)
        return None


def build_entry(sku_dir: Path):
    sku = sku_dir.name
    pdf_path = sku_dir / f"{sku}-datasheet.pdf"
    if not pdf_path.exists():
        print(f"  ⚠ {sku}: no PDF found, skipping")
        return None

    product = load_json(sku_dir / "product.json") or {}
    version_log = load_json(sku_dir / "version-log.json") or {}

    missing_meta = not product
    if missing_meta:
        print(f"  ⚠ {sku}: missing product.json — showing SKU only, "
              f"backfill with `wiki_tool.py datasheet --sku {sku} --force`")

    return {
        "sku": sku,
        "name": product.get("name") or sku,
        "family": product.get("family") or "General",
        "category": product.get("category") or "",
        "compatible_with": product.get("compatible_with") or [],
        "description": product.get("description") or "",
        "tags": product.get("tags") or [],
        "document_version": version_log.get("document_version", 1),
        "product_revision": version_log.get("product_revision", 1),
        "generated_at": version_log.get("generated_at", ""),
        "pdf_path": f"datasheets/{sku}/{sku}-datasheet.pdf",
        "pdf_size_bytes": pdf_path.stat().st_size,
        "needs_metadata_backfill": missing_meta,
    }


def main() -> int:
    if not DATASHEETS_DIR.exists():
        print(f"No datasheets/ directory at {DATASHEETS_DIR} — nothing to build.")
        MANIFEST_PATH.write_text(json.dumps(
            {"generated_at": "", "products": []}, indent=2) + "\n")
        return 0

    entries = []
    for sku_dir in sorted(p for p in DATASHEETS_DIR.iterdir() if p.is_dir()):
        entry = build_entry(sku_dir)
        if entry:
            entries.append(entry)

    entries.sort(key=lambda e: e["name"].lower())

    from datetime import datetime, timezone
    manifest = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "product_count": len(entries),
        "products": entries,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                              encoding="utf-8")

    backfill_needed = [e["sku"] for e in entries if e["needs_metadata_backfill"]]
    print(f"\n✓ Wrote {MANIFEST_PATH} — {len(entries)} product(s).")
    if backfill_needed:
        print(f"  {len(backfill_needed)} SKU(s) need a metadata backfill: "
              f"{', '.join(backfill_needed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
