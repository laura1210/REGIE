from ConnMongo import ConnMongo

class FacultyCheck:

    def __init__(self, faculty_id, course_code):
        self._id = faculty_id
        self._code = course_code

    def check(self):
        db = ConnMongo().conn()
        col = db["Course_Faculty"]
        doc = col.find({"_id": self._code})
        faculty = doc[0]["faculty"]
        if self._id in faculty:
            return True
        else:
            return False