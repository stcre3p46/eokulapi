"""Module for AvgMark model."""

from dataclasses import dataclass

from eokulapi.Models import from_int, str_to_float

ABOVE_AVG = 1
"""Indicates that the student's mark is above the class average"""

BELOW_AVG = -1
"""Indicates that the student's mark is below the class average"""

EQUAL_AVG = 0
"""Indicates that the student's mark is equal to the class average"""

NONE_AVG = 0
"""Indicates that the class average is not available"""


@dataclass
class AvgMark:
    """Average mark model."""

    avg_mark: float | None
    """Average mark of the class"""

    mark: float | None
    """Mark of the student"""

    state: int
    """State of the mark. See ABOVE_AVG, BELOW_AVG, EQUAL_AVG, NONE_AVG"""

    @classmethod
    def from_dict(cls, obj: dict):
        """Convert a dict to AvgMark object.

        Args:
            obj (dict): Object to be converted

        Returns:
            AvgMark: AvgMark object that is converted from dict
        """
        string_val = obj.get("value")

        if string_val is None:
            return cls(None, None, NONE_AVG)

        avg_mark = str_to_float(obj.get("avg_mark"))
        val = str_to_float(string_val)
        ac_val = from_int(obj.get("description_value"))

        return cls(avg_mark, val, ac_val)
