import unittest
from ConnMongo import ConnMongo
from RegisterCourse import RegisterCourse
from DropCourse import DropCourse

class DropCourseTest(unittest.TestCase):

    def tearDown(self):
        # change back to original database
        db = ConnMongo().conn()
        col1 = db['Course_Student']
        col1.update_one({"_id": 'MPCS_51410'}, {"$set": {'student': [10000000,20000000,40000000,50000000]}})
        col1.update_one({"_id": 'PPHA_36800'}, {"$set": {'student': [10000000,20000000,30000000,40000000,50000000]}})     
        col2 = db['Student_Course']
        col2.update_one({"_id": 10000000}, {"$set": {'course': ['MPCS_51410','MPCS_52553','PPHA_36800','CAPP_30300','MPCS_55001']}})
        col2.update_one({"_id": 30000000}, {"$set": {'course': ['MPCS_52553','PPHA_36800']}})
        col2.update_one({"_id": 60000000}, {"$set": {'course': ['MPCS_55001']}})
        col3 = db['Waitlist']
        col3.delete_one({"_id": 'PPHA_36800'})

    def test_exist(self):
        drop = DropCourse(60000000,'PPHA_36800')
        self.assertEqual(drop.drop_course(), "you don't register for this course")

    def test_late(self):
        drop = DropCourse(10000000,'CAPP_30300')
        self.assertEqual(drop.drop_course(), "too late to drop")

    def test_simple(self):
        # test case for no student is in the waitlist
        drop = DropCourse(10000000,'MPCS_51410')
        self.assertEqual(drop.drop_course(), "drop successfully")

        db = ConnMongo().conn()
        col1 = db['Course_Student']
        doc1 = col1.find({"_id": "MPCS_51410"})
        student = doc1[0]['student']
        self.assertEqual(student, [20000000,40000000,50000000])

        col2 = db['Student_Course']
        doc2 = col2.find({"_id": 10000000})
        course = doc2[0]['course']
        self.assertEqual(course, ['MPCS_52553','PPHA_36800','CAPP_30300','MPCS_55001'])

    def test_complex(self):
        # test case for someone is in the waitlist

        # new registration to put someone in the waitlist
        register = RegisterCourse(60000000, "PPHA_36800")
        res = register.register_course()
        
        drop = DropCourse(30000000,'PPHA_36800')
        self.assertEqual(drop.drop_course(), "drop successfully")

        db = ConnMongo().conn()
        col1 = db['Course_Student']
        doc1 = col1.find({"_id": "PPHA_36800"})
        student = doc1[0]['student']
        self.assertEqual(student, [10000000,20000000,40000000,50000000,60000000])

        col2 = db['Student_Course']
        doc2 = col2.find({"_id": 60000000})
        course = doc2[0]['course']
        self.assertEqual(course, ['MPCS_55001','PPHA_36800'])


if __name__ == '__main__':
    unittest.main()

