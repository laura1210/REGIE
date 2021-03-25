from ConnSQL import ConnSQL
from ConnMongo import ConnMongo
from ViewCourse import ViewCourse

class DropCourse:

    def __init__(self, student_id, course_code):
        self._id = student_id
        self._code = course_code

    def exist(self):
        # check if the course in the student's course list
        viewer = ViewCourse(self._id, 'Student')
        courses = viewer.view_course()
        return self._code in courses

    def graded(self):
        # check if the course has been graded
        db = ConnSQL().conn()
        cursor = db.cursor()
        query = "SELECT COUNT(*) FROM Grade WHERE course_code = '"+self._code+\
                "' AND student_id = "+str(self._id)
        cursor.execute(query)
        return bool(cursor.fetchone()[0])

    def drop_course(self):
        if not self.exist():
            return "you don't register for this course"
        elif self.graded():
            return "too late to drop"

        db = ConnMongo().conn()
        # delete the student from the course's student list
        col1 = db['Course_Student']
        col1.update_one({"_id": self._code}, {"$pull": {'student': self._id}})
        # delete the course from the student's course list
        col2 = db['Student_Course']
        col2.update_one({"_id": self._id}, {"$pull": {'course': self._code}})
        # check waitlist
        col3 = db['Waitlist']
        wait_exist = col3.count_documents({"_id": self._code})
        # if someone is in the waitlist, 
        # add the first student in the waitlist to the current student list 
        # and remove him from the waitlist
        if wait_exist:
            student = col3.find({"_id": self._code})[0]['student'][0]
            col3.update_one({"_id": self._id}, {"$pop": {'course': -1}})
            col1.update_one({"_id": self._code}, {"$push": {"student": student}})
            col2.update_one({"_id": student}, {"$push": {'course': self._code}})
        return "drop successfully"