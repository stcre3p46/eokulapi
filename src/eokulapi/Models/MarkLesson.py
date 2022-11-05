from dataclasses import dataclass
from typing import Any

from eokulapi.Models import from_int, from_str, str_to_float


@dataclass
class MarkLesson:
    lesson: str
    lesson_id: str
    lesson_weekly_period: int
    term: int
    isExempt: bool
    odv: Any
    tpu: Any
    score: float
    sozlu: dict[int, float]
    yazili: dict[int, float]

    @staticmethod
    def from_dict(obj: dict) -> "MarkLesson":
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

        return MarkLesson(ders, ders_kodu, ders_saati, donem, muaf, odv, tpu, puan, sozlu, yazili)
