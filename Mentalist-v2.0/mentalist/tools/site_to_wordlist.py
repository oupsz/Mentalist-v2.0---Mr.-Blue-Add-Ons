#!/usr/bin/env python3
"""
Fetch an HTML page (via requests), extract visible text (BeautifulSoup),
clean it and write a wordlist (one word per line). Returns the word count.
"""

from pathlib import Path
import string
import re

import requests
from bs4 import BeautifulSoup


NAME_RE = re.compile(r"^[A-ZÁÉÍÓÚÂÊÎÔÛÄËÏÖÜÃÕÇ][a-záéíóúâêîôûäëïöüãõç'-]{1,}$")


def _make_wordlist_from_text(text: str, remove_punct: bool = False, to_lower: bool = False):
    if remove_punct:
        trans = str.maketrans("", "", string.punctuation)
        text = text.translate(trans)
    if to_lower:
        text = text.lower()
    words = [w for w in text.split() if w.strip()]
    return list(dict.fromkeys(words))


def fetch_and_build(
    url: str,
    output_path: Path,
    remove_punct: bool = True,
    to_lower: bool = True,
    filter_first_names: bool = False,
    timeout: int = 15
) -> int:
    """
    Fetch the URL, extract visible text and write a wordlist to output_path.
    Returns number of words written.
    """
    r = requests.get(url, timeout=timeout, headers={"User-Agent": "mentalist-site-to-wordlist/2.0"})
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    soup = BeautifulSoup(r.text, "html.parser")

    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "svg", "iframe"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    words = _make_wordlist_from_text(
        text,
        remove_punct=remove_punct,
        to_lower=to_lower if not filter_first_names else False
    )
    if filter_first_names:
        words = [w for w in words if NAME_RE.match(w)]
    output_path.write_text("\n".join(words) + ("\n" if words else ""), encoding="utf-8")
    return len(words)
