# pytest unit tests for eokulapi module

from os import getenv

from dotenv import load_dotenv

from eokulapi import EokulAPI

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
    assert "EREN A" in student.name, "Student name is not what expected"


def test_get_student_grades():
    api = EokulAPI(uid)
    student = api.students[0]
    assert 1 <= student.grade <= 12, "Student grade is not what expected"


def test_get_student_class():
    import re

    api = EokulAPI(uid)
    student = api.students[0]
    assert re.match(
        r"^\d{1,2}\.Sınıf$", student.class_
    ), "Student class is not what expected"


def test_get_student_tckn():
    api = EokulAPI(uid)
    student = api.students[0]

    # check tckn is valid
    tckn = student.tckn
    stckn = str(tckn)

    assert len(stckn) == 11, "TCKN is not 11 digits long"
    assert (tckn % 10) == (sum([int(i) for i in stckn[:-1]]) % 10), "TCKN is not valid"

    chksum = (
        sum([int(stckn[i]) for i in range(0, 9, 2)]) * 7
        - sum([int(stckn[i]) for i in range(1, 9, 2)])
    ) % 10

    assert chksum == int(stckn[9]), "TCKN is not valid"
    assert (sum([int(stckn[i]) for i in range(10)]) % 10) == int(
        stckn[10]
    ), "TCKN is not valid"


def test_get_student_photo():
    api = EokulAPI(uid)
    student = api.students[0]
    assert student.photo, "Student photo is empty"


def test_update_student_data():
    api = EokulAPI(uid)
    student = api.students[0]
    api.update_student_data(student)


def test_get_student_endterm_marks():
    api = EokulAPI(uid)
    student = api.students[0]

    api._update_endterm_marks(student)

    assert student.endterm_marks.data, "Student's endterm marks is empty"
    assert student.endterm_marks.data[
        0
    ].academic_year, "Student's 1st endterm mark academic year is empty"
    assert student.endterm_marks.data[
        0
    ].endterm_mark, "Student's 1st endterm mark is empty"
