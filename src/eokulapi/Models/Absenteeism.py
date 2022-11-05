from dataclasses import dataclass
from datetime import date

from eokulapi.Models import from_float, from_str, month_to_int, str_to_date


@dataclass
class Absenteeism:
    date: date
    count: float
    reason: str

    @staticmethod
    def from_dict(obj: dict) -> "Absenteeism":
        date_list = from_str(obj.get("Gun")).split()
        date_str = f"{date_list[0]:02};{month_to_int(date_list[1]):02};{date_list[2]}"
        date = str_to_date(date_str)

        count = from_float(obj.get("GunSayi"))
        reason = from_str(obj.get("Nedeni"))

        return Absenteeism(date, count, reason)
