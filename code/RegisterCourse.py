from ConnSQL import ConnSQL
from ConnMongo import ConnMongo
from ViewCourse import ViewCourse

class RegisterCourse:

    def __init__(self, student_id, course_code):
        self._id = student_id
        self._code = course_code

    def exist(self):
        # check if the student has already registered for the course
        viewer = ViewCourse(self._id, 'Student')
        courses = viewer.view_course()
        return self._code in courses

    def register_course(self):
        if self.exist():
            return "already in the course"

        # get student number limit and permission requirement data
        db1 = ConnSQL().conn()
        cursor = db1.cursor()
        query = "SELECT max_num, permission_required FROM Course WHERE course_code = '"+str(self._code)+"'"
        cursor.execute(query)
        max_num, permission_required = cursor.fetchone()

        db2 = ConnMongo().conn()
        col1 = db2['Course_Student']
        doc1 = col1.find({"_id": self._code})
        curr_num = len(doc1[0]['student'])

        # add the student to request list if permission required
        if permission_required:
            col_name = "Request"
            res = "wait instructor permission"
        # add the student to the current student list
        # and add the course to the student's course list
        # if current students' number doesn't exceed the limit
        elif curr_num < max_num:
            col = db2['Student_Course']
            col.update_one({"_id": self._id}, {"$push": {"course": self._code}})
            col_name = "Course_Student"
            res = "register successfully"
        # add the student to the waitlist if student number exceeds limit
        else:
            col_name = "Waitlist"
            res = "add to wait list"

        col2 = db2[col_name]
        exist = col2.count_documents({"_id": self._code})
        if not exist:
            col2.insert_one({"_id": self._code, "student": [self._id]})
        else:
            col2.update_one({"_id": self._code}, {"$push": {"student": self._id}})

        return res