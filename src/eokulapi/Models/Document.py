from dataclasses import dataclass

from eokulapi.Models import from_str


@dataclass
class Document:
    doc_type: str
    term: str
    grade: str

    @staticmethod
    def from_dict(obj: dict) -> "Document":
        tur = from_str(obj.get("BelgeTuru"))
        donem = from_str(obj.get("Donemi"))
        sinif = from_str(obj.get("Sinifi"))
        return Document(tur, donem, sinif)
