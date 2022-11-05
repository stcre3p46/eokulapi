from dataclasses import dataclass
from datetime import time

from eokulapi.Models import from_int, from_none, from_str, from_union, str_to_time


@dataclass
class Lesson:
    start: time
    end: time
    name: str
    nth: int
    teacher: str | None

    @staticmethod
    def from_dict(obj: dict) -> "Lesson":
        start = str_to_time(obj.get("Baslangic_Saati"))
        end = str_to_time(obj.get("Bitis_Saati"))
        name = from_str(obj.get("Ders"))
        nth = from_int(obj.get("KacinciDers"))
        teacher = from_union([from_str, from_none], obj.get("Ogretmen"))
        if isinstance(teacher, str) and teacher[0] == " ":
            teacher = teacher[1:]
        return Lesson(start, end, name, nth, teacher)
