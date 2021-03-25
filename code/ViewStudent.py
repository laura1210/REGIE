from ConnMongo import ConnMongo

class ViewStudent:

    def __init__(self, course_code):
        self._course_code = course_code

    def view_student(self):
        db = ConnMongo().conn()
        col = db["Course_Student"]
        doc = col.find({"_id": self._course_code})
        student = doc[0]["student"]
        return student