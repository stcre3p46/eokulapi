from dataclasses import dataclass

from eokulapi.Models import from_str, str_to_float


@dataclass
class EndtermMark:
    academic_year: str
    grade: str
    endterm_mark: float

    @staticmethod
    def from_dict(obj: dict) -> "EndtermMark":
        yil = from_str(obj.get("OGRETIMYILI"))
        sinif = from_str(obj.get("SINIF"))
        yilsonunot = str_to_float(obj.get("YILSONUNOTU"))
        return EndtermMark(yil, sinif, yilsonunot)
