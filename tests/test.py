# exit(0) # skip tests

from os import environ
from pprint import pprint

from dotenv import load_dotenv

from eokulapi.eokulapi import EokulAPI

load_dotenv()
user = EokulAPI(uid=environ["EOKUL_UID"])

st = user.students[0]

user.update_student_data(st)

user.student_dict[st.tckn] = (st, "anan")

user.update_student_data(st)

print(f"name: {st.name}")
print(f"number: {st.number}")
print(f"grade: {st.grade}")
print(f"class: {st.class_}")

pprint(st.marks)

pprint(st.class_exam_average)

pprint(st.exam_schedule)

pprint(st.absenteeism)

print("test is done")
