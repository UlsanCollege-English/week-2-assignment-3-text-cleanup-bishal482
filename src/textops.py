# src/textops.py

from collections import Counter

def unique_words_preserve_order(words):
    """Return unique words while preserving their first occurrence order."""
    seen = set()
    result = []
    for w in words:
        if w not in seen:
            seen.add(w)
            result.append(w)
    return result


def top_k_frequent_first_tie(words, k):
    """
    Return top-k frequent words.
    If counts tie, earlier first appearance wins.
    """
    if k <= 0:
        raise ValueError("k must be positive")

    counts = Counter(words)

    # Record first index of each word
    first_index = {}
    for i, w in enumerate(words):
        if w not in first_index:
            first_index[w] = i

    # Sort by frequency (desc), then first appearance (asc)
    sorted_words = sorted(
        counts.keys(),
        key=lambda w: (-counts[w], first_index[w])
    )

    return sorted_words[:k]


def redact_words(words, banned):
    """Replace banned words with *** in the list of words."""
    banned_set = set(banned)
    return ["***" if w in banned_set else w for w in words]
