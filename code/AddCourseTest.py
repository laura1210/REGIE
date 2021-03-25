import unittest
from ConnSQL import ConnSQL
from AddCourse import AddCourse

class AddCourseTest(unittest.TestCase):

    def tearDown(self):
        db = ConnSQL().conn()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Course WHERE course_code = 'CAPP_30121';")
        db.commit()

    def test(self):
        adder = AddCourse('CAPP_30121','Python Programming',60,'Tue','Keller',0)
        self.assertEqual(adder.add_course(), "add CAPP_30121")
        
        db = ConnSQL().conn()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Course WHERE course_code = 'CAPP_30121';")
        code, name, max_num, time, loc, permission = cursor.fetchone()
        self.assertEqual(code, 'CAPP_30121')
        self.assertEqual(name, 'Python Programming')
        self.assertEqual(max_num, 60)
        self.assertEqual(time, 'Tue')
        self.assertEqual(loc, 'Keller')
        self.assertEqual(permission, 0)

if __name__ == '__main__':
    unittest.main()

