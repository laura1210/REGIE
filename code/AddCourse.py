from ConnSQL import ConnSQL

class AddCourse:

    def __init__(self, code, name, max_num, time, loc, permission):
        self._code = code
        self._name = name
        self._max_num = max_num
        self._time = time
        self._loc = loc
        self._permission = permission

    def add_course(self):
        db = ConnSQL().conn()
        cursor = db.cursor()
        insert = "INSERT INTO Course VALUES('" +\
                 "','".join([self._code,self._name,str(self._max_num),\
                           self._time,self._loc,str(self._permission)]) +\
                 "');"
        cursor.execute(insert)
        db.commit()
        return "add " + self._code