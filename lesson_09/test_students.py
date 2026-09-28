from sqlalchemy import text

from db import db


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:new_user_id, :new_level, :new_form, :new_subject_id)
    """)
    connection.execute(sql, {
        "new_user_id": 999999,
        "new_level": "Beginner",
        "new_form": "personal",
        "new_subject_id": 1,
    })

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("""
        UPDATE student
        SET level = :new_level
        WHERE user_id = :uid
    """)
    connection.execute(sql, {"new_level": "Upper-Intermediate", "uid": 999999})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM student WHERE user_id = :uid")
    connection.execute(sql, {"uid": 999999})

    transaction.commit()
    connection.close()
