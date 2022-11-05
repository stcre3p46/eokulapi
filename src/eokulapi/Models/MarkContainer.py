from dataclasses import dataclass

from eokulapi.Models import from_list
from eokulapi.Models.MarkLesson import MarkLesson


@dataclass
class MarkContainer:
    avg: float | None
    data: list[MarkLesson]

    @staticmethod
    def from_dict(obj: dict) -> "MarkContainer":
        liste = from_list(MarkLesson.from_dict, obj.get("notListesi"))
        ort = float(
            sum([lesson.lesson_weekly_period * lesson.score for lesson in liste])
            / sum([lesson.lesson_weekly_period for lesson in liste])
        )
        return MarkContainer(ort, liste)
