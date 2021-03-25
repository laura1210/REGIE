import unittest
from ConnMongo import ConnMongo
from ApproveRequest import ApproveRequest
from RegisterCourse import RegisterCourse

class ApproveRequestTest(unittest.TestCase):

    def setUp(self):
        # a new register for a course need permission
        register = RegisterCourse(30000000, 'MPCS_51410')
        register.register_course()

    def tearDown(self):
        # change back to original database
        db = ConnMongo().conn()
        col1 = db['Course_Student']
        col1.update_one({"_id": 'MPCS_51410'}, {"$set": {'student': [10000000,20000000,40000000,50000000]}})
        col2 = db['Student_Course']
        col2.update_one({"_id": 30000000}, {"$set": {'course': ['MPCS_52553','PPHA_36800']}})
        col3 = db['Request']
        col3.delete_one({"_id": 'MPCS_51410'})

    def test_faculty(self):
        approve = ApproveRequest(10000000, 60000000, 'PPHA_36800')
        self.assertEqual(approve.approve_request(), "you don't teach this course")

    def test_student(self):
        approve = ApproveRequest(10000000, 60000000, 'MPCS_51410')
        self.assertEqual(approve.approve_request(), "this student doesn't need permission")

    def test_right(self):
        approve = ApproveRequest(10000000, 30000000, 'MPCS_51410')
        self.assertEqual(approve.approve_request(), "approve request successfully")

        # add new student to Course_Student
        db = ConnMongo().conn()
        col1 = db['Course_Student']
        doc1 = col1.find({"_id": "MPCS_51410"})
        student = doc1[0]['student']
        self.assertEqual(student, [10000000,20000000,40000000,50000000,30000000])

        # add new course to student's course list
        col2 = db['Student_Course']
        doc2 = col2.find({"_id": 30000000})
        course = doc2[0]['course']
        self.assertEqual(course, ['MPCS_52553','PPHA_36800','MPCS_51410'])


if __name__ == '__main__':
    unittest.main()

