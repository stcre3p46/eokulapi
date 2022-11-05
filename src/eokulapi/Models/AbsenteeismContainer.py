from dataclasses import dataclass

from eokulapi.Models import from_float, from_list, from_str, month_to_int, str_to_float
from eokulapi.Models.Absenteeism import Absenteeism


@dataclass
class AbsenteeismContainer:
    excused_count: float
    not_excused_count: float
    by_month: dict[int, float]
    data: list[Absenteeism]

    @staticmethod
    def from_dict(obj: dict) -> "AbsenteeismContainer":
        by_month: dict = {}
        ozurlu = str_to_float(obj.get("Ozurlu"))
        ozursuz = str_to_float(obj.get("Ozursuz"))

        for abs in obj.get("DevamsizlikGrafikler"):
            ay = from_str(abs.get("Ay"))
            gun = from_float(abs.get("GunSayisi"))
            ay_int = month_to_int(ay)
            by_month[ay_int] = gun

        liste = from_list(Absenteeism.from_dict, obj.get("DevamsizlikListesi"))
        return AbsenteeismContainer(ozurlu, ozursuz, by_month, liste)
