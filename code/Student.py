from ChangePass import ChangePass
from ViewCourse import ViewCourse
from RegisterCourse import RegisterCourse
from DropCourse import DropCourse
from ViewTranscript import ViewTranscript

class Student:
	def __init__(self, id_, name, password, email, courses, grades):
        self._id = id_
        self._name = name
        self._password = password
        self._email = email

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def change_pass(self, new):
        changer = ChangePass(self._id, 'Student', self._password, new)
        return changer.change_pass()

    def get_email(self):
    	return self._email

    def view_courses(self):
        viewer = ViewCourse(self.id_, 'Student')
        return viewer.view_course()

    def register_course(self, course_code):
        register = RegisterCourse(self._id, course_code)
        return register.register_course()

    def drop_course(self, course_code):
        drop = DropCourse(self._id, course_code)
        return drop.drop_course()

    def view_transcript(self):
        viewer = ViewTranscript(self._id)
        return viewer.view_trans()