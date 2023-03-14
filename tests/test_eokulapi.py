# pytest unit tests for eokulapi module

from os import getenv

import pytest
from dotenv import load_dotenv

from eokulapi.eokulapi import EokulAPI

load_dotenv()

uid = getenv("EOKUL_UID")


def test_login():
    api = EokulAPI(uid)
    api._update_student_list()


def test_anon_login():
    api = EokulAPI()
    api._update_student_list()


def test_get_student():
    api = EokulAPI(uid)
    student = api.students[0]
    assert "EREN A" in student.name


def test_get_student_grades():
    api = EokulAPI(uid)
    student = api.students[0]
    assert 1 <= student.grade <= 12


def test_get_student_class():
    import re
    api = EokulAPI(uid)
    student = api.students[0]
    assert re.match(r"^\d{1,2}\.Sınıf$", student.class_)


def test_get_student_tckn():
    api = EokulAPI(uid)
    student = api.students[0]

    # check tckn is valid
    tckn = student.tckn
    stckn = str(tckn)

    assert len(stckn) == 11
    assert (tckn % 10) == (sum([int(i) for i in stckn[:-1]]) % 10)

    chksum = (
        sum([int(stckn[i]) for i in range(0, 9, 2)]) * 7
        - sum([int(stckn[i]) for i in range(1, 9, 2)])
    ) % 10

    assert chksum == int(stckn[9])
    assert (sum([int(stckn[i]) for i in range(10)]) % 10) == int(stckn[10])

def test_get_student_photo():
    api = EokulAPI(uid)
    student = api.students[0]
    assert student.photo != b""

def test_update_student_data():
    api = EokulAPI(uid)
    student = api.students[0]
    api.update_student_data(student)
    assert True

def test_get_student_endterm_marks():
    api = EokulAPI(uid)
    student = api.students[0]

    api._update_endterm_marks(student)

    assert student.endterm_marks.data
    assert student.endterm_marks.data[0].academic_year
    assert student.endterm_marks.data[0].endterm_mark
