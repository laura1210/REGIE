from ConnMongo import ConnMongo

class ViewCourse:

    def __init__(self, id_, type_):
        self._id = id_
        self._type = type_

    def view_course(self):
        db = ConnMongo().conn()
        col = db[self._type + "_Course"]
        doc = col.find({"_id": self._id})
        course = doc[0]["course"]
        return course