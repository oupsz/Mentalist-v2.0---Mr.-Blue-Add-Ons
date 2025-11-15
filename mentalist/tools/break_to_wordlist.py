#!/usr/bin/env python3
"""
Break text → Wordlist
---------------------
This utility converts plain text (or all files in a directory) into
a clean wordlist — one word per line.

Options:
- Optionally remove punctuation.
- Optionally convert to lowercase.
- Automatically removes duplicate words while preserving order.
"""

from pathlib import Path
import string


def _read_input_text(path: Path) -> str:
    """
    Reads input from a file or directory.
    If a directory is provided, all files are concatenated in sorted order.
    """
    if path.is_dir():
        parts = []
        for p in sorted(path.iterdir()):
            if p.is_file():
                parts.append(p.read_text(encoding="utf-8", errors="ignore"))
        return "\n".join(parts)
    elif path.is_file():
        return path.read_text(encoding="utf-8", errors="ignore")
    else:
        raise FileNotFoundError(path)


def _make_wordlist_from_text(text: str, remove_punct: bool = False, to_lower: bool = False):
    """
    Splits text into words and applies basic cleanup options.
    - remove_punct: strips punctuation characters.
    - to_lower: converts all text to lowercase.
    - Removes duplicates while preserving order.
    """
    if remove_punct:
        trans = str.maketrans("", "", string.punctuation)
        text = text.translate(trans)
    if to_lower:
        text = text.lower()

    # Split on whitespace and remove empty tokens
    words = [w for w in text.split() if w.strip()]

    # Deduplicate while preserving order
    return list(dict.fromkeys(words))


def build_wordlist(input_path: Path, output_path: Path, remove_punct=False, to_lower=False) -> int:
    """
    Builds a wordlist from the given input and writes it to output_path.

    Args:
        input_path (Path): File or directory containing text.
        output_path (Path): Destination file for the resulting wordlist.
        remove_punct (bool): Whether to remove punctuation characters.
        to_lower (bool): Whether to convert to lowercase.

    Returns:
        int: The total number of words written.
    """
    text = _read_input_text(input_path)
    words = _make_wordlist_from_text(text, remove_punct=remove_punct, to_lower=to_lower)
    output_path.write_text("\n".join(words) + ("\n" if words else ""), encoding="utf-8")
    return len(words)
