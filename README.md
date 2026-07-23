# Argon 40 — Product Datasheets

Official,product datasheets for [Argon 40](https://argon40.com) —
premium enclosures, expansion boards, and accessories for Raspberry Pi single-board computers.

This repository is **public and view-only**. Every datasheet here is generated and published
automatically from Argon 40's internal product database; it is not edited by hand.

---

## 📄 Find a datasheet

Datasheets are organized one folder per product, keyed by SKU:

```
datasheets/
  ARG-ONE-V5/
    ARG-ONE-V5-datasheet.pdf      ← the datasheet
    version-log.json              ← full revision history
  ARG-ONE-V5-NVME/
    ARG-ONE-V5-NVME-datasheet.pdf
    version-log.json
  ...
```

- **PDF** — the current datasheet for that product (identity, specifications,
  compatibility, features, and a Document Control block).
- **`version-log.json`** — the complete revision history for that datasheet
  (see [Versioning](#-versioning) below).

> **Tip:** the SKU is on every Argon 40 product page and box. Browse the
> [`datasheets/`](datasheets/) folder and open the folder matching your SKU.

<!-- If GitHub Pages is enabled on this repo, add the browsable link here:
Browse online: https://argon40tech.github.io/argon-datasheets/ -->

---

## 🔢 Versioning

Each datasheet PDF carries a **Document Control** block with two independent numbers:

| Field | Meaning |
|---|---|
| **Document version** | Increments every time the datasheet PDF is regenerated. |
| **Product revision** | Increments only when the underlying **product data actually changes** (specs, dimensions, identity, compatibility, etc.). |

So two PDFs can share the same *product revision* (the product hasn't changed) while having
different *document versions* (the document was re-rendered). The PDF's Document Control block
points to the matching entry in `version-log.json`, where the full change history lives:

```json
{
  "document_version": 3,
  "product_revision": 2,
  "generated_at": "2026-07-23 04:00 UTC",
  "content_hash": "…",
  "history": [
    { "document_version": 3, "product_revision": 2,
      "generated_at": "…", "remarks": ["dimensions_cm: 10 x 4 cm → 10 x 4 x 16.5 cm"] }
  ]
}
```

If a product's data hasn't changed, no new datasheet is generated — so a bump in
*document version* always reflects a genuine regeneration.

---

## ✅ Data sources & accuracy

Each datasheet consolidates and cross-checks several internal sources — the master product
list, the product catalog, and product manuals — into a single validated view before the PDF
is rendered. Where sources disagree, the value is resolved by a human before publishing, so the
figures you see have been reconciled rather than pulled blindly from one place.

Every value in a datasheet is drawn from Argon 40's own product records. If you spot something
that looks off, please let us know (see below) — corrections flow back through the internal
database and the datasheet is regenerated.

---

## 📦 Products covered

Argon 40's Raspberry Pi hardware lines, including:

- **Argon ONE** family (V5, V3, V2, M.2 NVMe variants) — aluminium Pi enclosures
- **Argon NEO** family — slim cases for Pi 5, Pi 4, and Pi Zero
- **Argon EON** — Pi NAS enclosure
- **Argon THRML** — active coolers and thermal solutions
- **Argon Industria** — industrial enclosures, HMI displays, and expansion boards
- **Argon PWR / POE+ / PSU** — power management and power supplies
- **Accessories** — POD modules, IR remote, fan HATs, GPIO breakouts, cables

See the [`datasheets/`](datasheets/) folder for the full, current list.

---

## ⚖️ Usage

These datasheets are provided for reference. You're welcome to view, download, and share them.
For the most up-to-date product information, pricing, and availability, visit the official store.

- **Store:** [argon40.com](https://argon40.com)
- **Wiki / guides:** [wiki.argon40.com](https://wiki.argon40.com)
- **GitHub:** [github.com/Argon40Tech](https://github.com/Argon40Tech)
- **Datasheet corrections or questions:** [support@argon40.com](mailto:support@argon40.com)

---

<sub>This repository is generated automatically. Files are updated in place as products change —
do not open pull requests against datasheet files; contact support with corrections instead.</sub>
