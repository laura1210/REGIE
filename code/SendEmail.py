from ViewStudent import ViewStudent
from ConnSQL import ConnSQL
from FacultyCheck import FacultyCheck

class SendEmail:

    def __init__(self, faculty_id, course_code, subject, body):
        self._faculty_id = faculty_id
        self._course_code = course_code
        self._subject = subject
        self._body = body

    def send_email(self):
        checker = FacultyCheck(self._faculty_id, self._course_code)
        if not checker.check():
            print("you don't teach this course")
            return []
        else:
            students = ViewStudent("MPCS_51410").view_student()
            db = ConnSQL().conn()
            cursor = db.cursor()
            sent = []
            for s in students:
                cursor.execute("SELECT email FROM Student WHERE id = " + str(s))
                address = cursor.fetchone()[0]
                # send email to address with right subject and body
                sent.append(address)
            return sent