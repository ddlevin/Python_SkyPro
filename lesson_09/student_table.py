from sqlalchemy import create_engine, text


class StudentTable:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_student_by_id(self, user_id):
        conn = self.db.connect()
        result = conn.execute(
            text("SELECT * FROM student WHERE user_id = :uid"),
            {"uid": user_id},
        )
        row = result.mappings().first()
        conn.close()
        return row

    def add_student(self, user_id, level, education_form, subject_id):
        conn = self.db.connect()
        conn.execute(
            text(
                "INSERT INTO student "
                "(user_id, level, education_form, subject_id) "
                "VALUES (:uid, :lvl, :ef, :sid)"
            ),
            {
                "uid": user_id,
                "lvl": level,
                "ef": education_form,
                "sid": subject_id,
            },
        )
        conn.commit()
        conn.close()

    def update_student(
        self,
        user_id,
        level=None,
        education_form=None,
        subject_id=None,
    ):
        conn = self.db.connect()
        if level is not None:
            conn.execute(
                text(
                    "UPDATE student SET level = :lvl "
                    "WHERE user_id = :uid"
                ),
                {"lvl": level, "uid": user_id},
            )
        if education_form is not None:
            conn.execute(
                text(
                    "UPDATE student SET education_form = :ef "
                    "WHERE user_id = :uid"
                ),
                {"ef": education_form, "uid": user_id},
            )
        if subject_id is not None:
            conn.execute(
                text(
                    "UPDATE student SET subject_id = :sid "
                    "WHERE user_id = :uid"
                ),
                {"sid": subject_id, "uid": user_id},
            )
        conn.commit()
        conn.close()

    def delete_student(self, user_id):
        conn = self.db.connect()
        conn.execute(
            text("DELETE FROM student WHERE user_id = :uid"),
            {"uid": user_id},
        )
        conn.commit()
        conn.close()
