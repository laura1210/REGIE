from ChangePass import ChangePass
from ViewStudent import ViewStudent
from SendEmail import SendEmail
from ViewCourse import ViewCourse
from AssignGrade import AssignGrade
from ApproveRequest import ApproveRequest

class Faculty:
	def __init__(self, id_, name, password):
        self._id = id_
        self._name = name
        self._password = password

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def change_pass(self, new):
        changer = ChangePass(self._id, 'Faculty', self._password, new)
        return changer.change_pass()

    def view_students(self, course_code):
        viewer = ViewStudent(course_code)
        return viewer.view_student()

    def send_email(self, course_code, subject, body):
        sender = SendEmail(self._id, course_code, subject, body)
        return sender.send_email()

    def view_courses(self):
        viewer = ViewCourse(self.id_, 'Faculty')
        return viewer.view_course()

    def assgin_grade(self, course_code, student_id, grade):
        grader = AssignGrade(self._id, course_code, student_id, grade)
        return grader.assgin_grade()

    def approve_request(self, student_id, course_code):
        approve = ApproveRequest(self._id, student_id, course_code)
        return approve.approve_request()