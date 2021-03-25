from ConnSQL import ConnSQL

class ViewTranscript:

    def __init__(self, student_id):
        self._id = student_id

    def view_trans(self):
        db = ConnSQL().conn()
        cursor = db.cursor()
        query = "SELECT course_code, grade FROM Grade WHERE student_id=" + str(self._id)
        cursor.execute(query)
        trans = cursor.fetchall()
        return trans