import hashlib


def generate_hash(text: str) -> str:
    """
    Generate a SHA256 hash for an article.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()