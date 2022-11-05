from dataclasses import dataclass
from datetime import date
from typing import Union

from eokulapi.Models import from_int, from_str, month_to_int, str_to_date


@dataclass
class ExamSchedule:
    isPast: bool
    date: date
    lesson: str

    @staticmethod
    def from_dict(obj: dict) -> Union["ExamSchedule", None, list["ExamSchedule"]]:
        dtype = from_int(obj.get("Liste"))
        if dtype == 2:
            isPast = False
            gun = from_str(obj.get("Ders")).split()
            ders = from_str(obj.get("Gun"))
        elif dtype == 3:
            isPast = True
            gun = from_str(obj.get("Gun")).split()
            ders = from_str(obj.get("Ders"))
        else:
            return None
        date_str = f"{gun[0]:02};{month_to_int(gun[1]):02};{gun[2]:04}"
        dt = str_to_date(date_str)

        if dtype == 3:
            return [ExamSchedule(isPast, dt, d) for d in ders.split("|")]

        return ExamSchedule(isPast, dt, ders)
