from dataclasses import dataclass

from eokulapi.Models import from_int, from_str
from eokulapi.Models.AvgMark import AvgMark


@dataclass
class AvgMarkLesson:
    lesson_name: str
    term: int
    marks: dict[int, AvgMark]

    @staticmethod
    def from_dict(obj: dict) -> "AvgMarkLesson":
        ders = from_str(obj.get("DERS"))
        donem = from_int(int(from_str(obj.get("DONEM"))))
        marks = {}
        for i in range(1, 7):
            mark = AvgMark.from_dict(
                {
                    "value": obj.get(f"Y{i}"),
                    "description": obj.get(f"Y{i}ACIKLAMA"),
                    "description_value": obj.get(f"Y{i}ACIKLAMADEGER"),
                    "avg_mark": obj.get(f"Y{i}SUBEORT"),
                }
            )
            marks[i] = mark
            return AvgMarkLesson(ders, donem, marks)
