from dataclasses import dataclass


@dataclass(frozen=True)
class Source:
    document_id: str
    filename: str
    filepath: str
    page: int
    content: str
