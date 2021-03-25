import unittest
from ConnMongo import ConnMongo
from RegisterCourse import RegisterCourse

class RegisterCourseTest(unittest.TestCase):

    def tearDown(self):
        # change back to original database
        db = ConnMongo().conn()
        col1 = db['Course_Student']
        col1.update_one({"_id": 'MPCS_52553'}, {"$set": {'student': [10000000,30000000,50000000]}})
        col2 = db['Student_Course']
        col2.update_one({"_id": 60000000}, {"$set": {'course': ['MPCS_55001']}})
        col3 = db['Request']
        col3.delete_one({"_id": 'CAPP_30300'})
        col4 = db['Waitlist']
        col4.delete_one({"_id": 'PPHA_36800'})

    def test_exist(self):
        register = RegisterCourse(10000000, "MPCS_51410")
        self.assertEqual(register.register_course(), "already in the course")

    def test_studentlist(self):
        register = RegisterCourse(60000000, "MPCS_52553")
        res = register.register_course()
        self.assertEqual(res, "register successfully")

        db = ConnMongo().conn()
        col1 = db['Course_Student']
        doc1 = col1.find({"_id": "MPCS_52553"})
        student = doc1[0]['student']
        self.assertEqual(student, [10000000,30000000,50000000,60000000])

        col2 = db['Student_Course']
        doc2 = col2.find({"_id": 60000000})
        course = doc2[0]['course']
        self.assertEqual(course, ['MPCS_55001','MPCS_52553'])

    def test_request(self):
        register = RegisterCourse(60000000, "CAPP_30300")
        res = register.register_course()
        self.assertEqual(res, "wait instructor permission")

        db = ConnMongo().conn()
        col = db['Request']
        doc = col.find({"_id": "CAPP_30300"})
        student = doc[0]['student']
        self.assertEqual(student, [60000000])

    def test_waitlist(self):
        register = RegisterCourse(60000000, "PPHA_36800")
        res = register.register_course()
        self.assertEqual(res, "add to wait list")

        db = ConnMongo().conn()
        col = db['Waitlist']
        doc = col.find({"_id": "PPHA_36800"})
        student = doc[0]['student']
        self.assertEqual(student, [60000000])

if __name__ == '__main__':
    unittest.main()

