from dataclasses import dataclass

from eokulapi.Models import from_int, str_to_float

ABOVE_AVG = 1
BELOW_AVG = ""
EQUAL_AVG = ""
NONE_AVG = ""


@dataclass
class AvgMark:
    avg_mark: float | None
    mark: float | None
    state: int

    @staticmethod
    def from_dict(obj: dict) -> "AvgMark":
        avg_mark = str_to_float(obj.get("avg_mark"))
        val = str_to_float(obj.get("value"))
        ac_val = from_int(obj.get("description_value"))

        return AvgMark(avg_mark, val, ac_val)
