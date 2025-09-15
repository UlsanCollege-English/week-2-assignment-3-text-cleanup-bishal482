"""Text Cleanup — Starter

You are processing a short list of words from a form.
Implement without mutating inputs.
"""
from typing import List
from collections import Counter


def unique_words_preserve_order(words: List[str]) -> List[str]:
    """Return first occurrences only (case-sensitive)."""
    seen = set()
    result = []
    for w in words:
        if w not in seen:
            seen.add(w)
            result.append(w)
    return result


def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    """Return up to k words ordered by frequency (high to low).

    For ties, earlier first-appearance wins.
    If k <= 0, raise ValueError.
    """
    if k <= 0:
        raise ValueError("k must be positive")

    count = Counter(words)
    first_index = {word: i for i, word in enumerate(words)}
    sorted_words = sorted(count.keys(), key=lambda w: (-count[w], first_index[w]))
    return sorted_words[:k]


def redact_words(words: List[str], redacted: List[str]) -> List[str]:
    """Return a new list with redacted words replaced by '***'."""
    redacted_set = set(redacted)
    return ["***" if w in redacted_set else w for w in words]
