# 🧠 Mentalist v2.0

**Author:** Pedro Winícius L. Soares de Souza (aka Mr. Blue)

---

## 🔥 Overview
This update upgrades Mentalist to version **2.0**, introducing two new GUI tools and several stability improvements.

### New Features
#### 1. Break text → Wordlist
Convert any local text file or folder into a clean, deduplicated wordlist.

#### 2. Site Converter in Wordlist
Fetch a website, extract visible text (HTML cleaned), and automatically generate a wordlist file.  
✅ **New in this update:** Optional “Filter by First Names?” checkbox keeps only capitalized words (proper names) for OSINT-friendly wordlists.

---

## 🧩 Technical Changes
- New modules:
  - `mentalist/tools/break_to_wordlist.py`
  - `mentalist/tools/site_to_wordlist.py`
- Updated `controller.py`:
  - Added `on_break_to_wordlist()` and `on_site_to_wordlist()` methods.
  - Introduced `UrlFirstNamesDialog` and the new first-name filtering workflow.
- Updated `view/main.py`:
  - Added a **Tools** menu with both options.
  - Removed detachable “tear-off” submenus.
- Updated `tools/site_to_wordlist.py` with first-name regex filtering support.
- Fixed `locale.format` → `locale.format_string` compatibility.
- Version updated from **1.0 → 2.0**.

---

## ⚙️ Installation
Run the setup script from your terminal:

```bash
cd ~/Área\ de\ Trabalho/Mentalist-v2.0
./install.sh
```
