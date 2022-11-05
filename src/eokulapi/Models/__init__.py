from datetime import date, time
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> list[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def str_to_time(string: str) -> time:
    string = from_str(string)
    str_list = string.split(":")
    return time(hour=int(str_list[0]), minute=int(str_list[1]))


def str_to_date(string: str) -> date:
    string = from_str(string)
    str_list = string.split(";")
    return date(year=int(str_list[2]), month=int(str_list[1]), day=int(str_list[0]))


def str_to_float(string: str) -> float | None:
    string = from_str(string)

    if string == "":
        return None
    return float(from_str(string).replace(",", "."))


def month_to_int(month: str) -> int:
    match from_str(month).lower():
        case "ocak":
            return 1
        case "şubat":
            return 2
        case "mart":
            return 3
        case "nisan":
            return 4
        case "mayıs":
            return 5
        case "haziran":
            return 6
        case "temmuz":
            return 7
        case "ağustos":
            return 8
        case "eylül":
            return 9
        case "ekim":
            return 10
        case "kasım":
            return 11
        case "aralık":
            return 12
    raise AssertionError(f"{month} is not a month")


def day_to_int(day: str) -> int:
    match from_str(day).lower():
        case "pazartesi":
            return 0
        case "salı":
            return 1
        case "çarşamba":
            return 2
        case "perşembe":
            return 3
        case "cuma":
            return 4
        case "cumartesi":
            return 5
        case "pazar":
            return 6
    raise AssertionError(f"{day} is not a day")
