from ConnSQL import ConnSQL
from FacultyCheck import FacultyCheck

class AssignGrade:

    def __init__(self, faculty_id, course_code, student_id, grade):
        self._faculty_id = faculty_id
        self._course_code = course_code
        self._student_id = student_id
        self._grade = grade

    def exist(self):
        # check if grade already exist for the course
        db = ConnSQL().conn()
        cursor = db.cursor()
        query = "SELECT COUNT(*) FROM Grade WHERE course_code = '"+self._course_code+\
                "' AND student_id = "+str(self._student_id)
        cursor.execute(query)
        return bool(cursor.fetchone()[0])

    def assign_grade(self):
        checker = FacultyCheck(self._faculty_id, self._course_code)
        if not checker.check():
            return "you don't teach this course"
        else:
            db = ConnSQL().conn()
            cursor = db.cursor()
            # change already exist grade
            if self.exist():
                update = "UPDATE Grade SET grade = '"+self._grade+\
                         "' WHERE course_code = '"+self._course_code+\
                         "' AND student_id = "+str(self._student_id)
            # assign new grade
            else:
                update = "INSERT INTO Grade VALUES ('"+self._course_code+\
                         "', "+str(self._student_id)+\
                         ", '"+self._grade+"')"
            cursor.execute(update)
            db.commit()
            return "assign grade successfully"