from ChangePass import ChangePass
from AddCourse import AddCourse

class Administrator:
	def __init__(self, id_, name, password):
        self._id = id_
        self._name = name
        self._password = password

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def change_pass(self, new):
        changer = ChangePass(self._id, 'Administrator', self._password, new)
        return changer.change_pass()

    def add_course(self, code, name, max_num, time, loc, permission):
        adder = AddCourse(code, name, max_num, time, loc, permission)
        return adder.add_course()