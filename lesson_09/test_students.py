from db import get_connection_string
from student_table import StudentTable

db = StudentTable(get_connection_string())


CREATE_ID = 990000001
UPDATE_ID = 990000002
DELETE_ID = 990000003


def test_add_student():
    db.add_student(CREATE_ID, "Beginner", "personal", 1)

    db_student = db.get_student_by_id(CREATE_ID)
    assert db_student is not None
    assert db_student["level"] == "Beginner"
    assert db_student["education_form"] == "personal"
    assert db_student["subject_id"] == 1

    db.delete_student(CREATE_ID)


def test_update_student():
    db.add_student(UPDATE_ID, "Beginner", "personal", 1)

    db.update_student(
        UPDATE_ID,
        level="Upper-Intermediate",
        education_form="group",
        subject_id=2,
    )

    db_student = db.get_student_by_id(UPDATE_ID)
    assert db_student["level"] == "Upper-Intermediate"
    assert db_student["education_form"] == "group"
    assert db_student["subject_id"] == 2

    db.delete_student(UPDATE_ID)


def test_delete_student():
    db.add_student(DELETE_ID, "Elementary", "personal", 1)

    db.delete_student(DELETE_ID)

    db_student = db.get_student_by_id(DELETE_ID)
    assert db_student is None
