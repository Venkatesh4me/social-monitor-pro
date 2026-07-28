import hashlib


def generate_hash(title, url):
    text = f"{title}{url}"
    return hashlib.sha256(text.encode()).hexdigest()