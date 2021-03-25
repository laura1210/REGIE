from ConnSQL import ConnSQL

class ChangePass:

    def __init__(self, id_, type_, old, new):
        self._id = id_
        self._type = type_
        self._old = old
        self._new = new

    def change_pass(self):
        db = ConnSQL().conn()
        cursor = db.cursor()
        query = "SELECT password FROM "+self._type+" WHERE id = "+str(self._id)
        cursor.execute(query)
        right_pass = cursor.fetchone()[0]

        if self._old == right_pass:
            update = "UPDATE "+self._type+" SET password = '"+self._new+"' WHERE id = "+str(self._id)
            cursor.execute(update)
            db.commit()
            return "password changed"
        else:
            return "wrong password"