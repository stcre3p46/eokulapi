from dataclasses import dataclass
from typing import Iterable, Optional

from eokulapi.Models import from_list
from eokulapi.Models.ExamSchedule import ExamSchedule


def _flatten(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in _flatten(item):
                yield x
        else:
            yield item


@dataclass
class ExamScheduleContainer:
    data: Optional[list[ExamSchedule]]

    @staticmethod
    def from_dict(obj: dict) -> "ExamScheduleContainer":
        schedule_list = from_list(ExamSchedule.from_dict, obj.get("SinavTarihleriListesi"))
        schedule_list = list(filter(lambda item: item is not None, _flatten(schedule_list)))

        return ExamScheduleContainer(schedule_list)
