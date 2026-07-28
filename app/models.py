from dataclasses import dataclass


@dataclass
class Article:
    website: str
    title: str
    url: str
    summary: str = ""
    published: str = ""
    author: str = ""
    hash: str = ""