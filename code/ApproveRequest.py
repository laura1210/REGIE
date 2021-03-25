from ConnMongo import ConnMongo
from ViewCourse import ViewCourse

class ApproveRequest:

    def __init__(self, faculty_id, student_id, course_code):
        self._faculty_id = faculty_id
        self._student_id = student_id
        self._code = course_code

    def check_course(self):
        # check if the faculty is an instructor for this course
        viewer = ViewCourse(self._faculty_id, 'Faculty')
        courses = viewer.view_course()
        return self._code in courses

    def check_student(self):
        # check if the student has requested permission
        db = ConnMongo().conn()
        col = db['Request']
        if not col.count_documents({"_id": self._code}):
            return False
        req = col.find({"_id": self._code})[0]['student']
        return self._student_id in req

    def approve_request(self):
        if not self.check_course():
            return "you don't teach this course"
        elif not self.check_student():
            return "this student doesn't need permission"

        db = ConnMongo().conn()
        # remove student from the request list
        col1 = db['Request']
        col1.update_one({"_id": self._code}, {"$push": {'student': self._student_id}})
        col2 = db['Waitlist']
        wait_exist = col2.count_documents({"_id": self._code})
        # add student to waitlist if exceed student number limit
        if wait_exist:
            col2.update_one({"_id": self._code}, {"$push": {'student': self._student_id}})
        # add student to the current student list of the course
        # and add the course to the students' course list
        else:
            col3 = db['Course_Student']
            col3.update_one({"_id": self._code}, {"$push": {'student': self._student_id}})
            col4 = db['Student_Course']
            col4.update_one({"_id": self._student_id}, {"$push": {'course': self._code}})
        return "approve request successfully"