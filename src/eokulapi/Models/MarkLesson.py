from dataclasses import dataclass
from typing import Any

from eokulapi.Models import from_int, from_str, str_to_float


@dataclass
class MarkLesson:
    """Mark lesson model"""

    lesson: str
    """Name of the lesson"""
    lesson_id: str
    """ID of the lesson"""
    lesson_weekly_period: int
    """Weekly period count of the lesson"""
    term: int
    """Term of the lesson"""
    isExempt: bool
    """Whether the student is exempt from the lesson"""
    odv: Any
    """Not implemented. possibly a float"""
    tpu: Any
    """Not implemented. possibly a float"""
    score: float
    """Score of the student in the lesson"""
    sozlu: dict[int, float]
    """Dict of `sözlü` exam scores (Exam Number: Score)"""
    yazili: dict[int, float]
    """Dict of `yazılı` exam scores (Exam Number: Score)"""

    @classmethod
    def from_dict(cls, obj: dict):
        """Converts a dict to MarkLesson object

        Args:
            obj (dict): Object to be converted

        Returns:
            MarkLesson: MarkLesson object that is converted from dict
        """
        ders = from_str(obj.get("Ders"))
        ders_kodu = from_str(obj.get("DersKodu"))
        ders_saati = from_int(int(from_str(obj.get("DersSaati"))))
        donem = from_int(int(from_str(obj.get("Donem"))))
        muaf = False if from_str(obj.get("Muaf")) == "-" else True
        odv = obj.get("ODV")
        tpu = obj.get("TPU")
        puan = str_to_float(obj.get("PUANI"))

        sozlu: dict[int, float] = {}
        yazili: dict[int, float] = {}

        for i in range(1, 7):
            dat = from_str(obj.get(f"SZL{i}"))
            if dat:
                sozlu[i] = str_to_float(dat)
        for i in range(1, 7):
            dat = from_str(obj.get(f"Y{i}"))
            if dat:
                yazili[i] = str_to_float(dat)

        return cls(ders, ders_kodu, ders_saati, donem, muaf, odv, tpu, puan, sozlu, yazili)
