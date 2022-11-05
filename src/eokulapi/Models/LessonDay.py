from dataclasses import dataclass

from eokulapi.Models import day_to_int, from_list
from eokulapi.Models.Lesson import Lesson


@dataclass
class LessonDay:
    day_number: int
    LessonList: list[Lesson]

    @staticmethod
    def from_dict(obj: dict) -> "LessonDay":
        liste = from_list(Lesson.from_dict, obj.get("DersProgramiItemList"))
        day = day_to_int(obj.get("Gun"))
        return LessonDay(day, liste)
