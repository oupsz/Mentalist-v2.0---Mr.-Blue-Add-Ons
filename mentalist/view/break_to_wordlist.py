from pathlib import Path
import string

def _read_input_text(path: Path) -> str:
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

def _make_wordlist_from_text(text: str, remove_punct=False, to_lower=False):
    if remove_punct:
        trans = str.maketrans("", "", string.punctuation)
        text = text.translate(trans)
    if to_lower:
        text = text.lower()
    words = [w for w in text.split() if w.strip()]
    return list(dict.fromkeys(words))  # dedupe preservando ordem

def build_wordlist(input_path: Path, output_path: Path, remove_punct=False, to_lower=False) -> int:
    text = _read_input_text(input_path)
    words = _make_wordlist_from_text(text, remove_punct=remove_punct, to_lower=to_lower)
    output_path.write_text("\n".join(words) + ("\n" if words else ""), encoding="utf-8")
    return len(words)
