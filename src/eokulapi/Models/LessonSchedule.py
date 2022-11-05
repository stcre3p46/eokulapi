from dataclasses import dataclass

from eokulapi.Models import from_list
from eokulapi.Models.LessonDay import LessonDay


@dataclass
class LessonSchedule:
    data: list[LessonDay]

    @staticmethod
    def from_dict(obj: dict) -> "LessonSchedule":
        liste = from_list(LessonDay.from_dict, obj.get("DersProgramiListesi"))
        return LessonSchedule(liste)
