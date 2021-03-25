import unittest
from ConnSQL import ConnSQL
from ChangePass import ChangePass

class ChangePassTest(unittest.TestCase):

    def tearDown(self):
        db = ConnSQL().conn()
        cursor = db.cursor()
        cursor.execute("UPDATE Student SET password = 'laura_pass' WHERE id = 10000000")
        cursor.execute("UPDATE Faculty SET password = 'yue_pass' WHERE id = 40000000")
        db.commit()

    def test_student_wrong(self):
        db = ConnSQL().conn()
        cursor = db.cursor()
        changer = ChangePass(10000000, 'Student', 'laura_pas', 'abc')
        self.assertEqual(changer.change_pass(), "wrong password")

        cursor.execute("SELECT password FROM Student WHERE id = 10000000")
        now_pass = cursor.fetchone()[0]
        self.assertEqual(now_pass, 'laura_pass')

    def test_student_right(self):
        db = ConnSQL().conn()
        cursor = db.cursor()
        changer = ChangePass(10000000, 'Student', 'laura_pass', 'abc')
        self.assertEqual(changer.change_pass(), "password changed")

        cursor.execute("SELECT password FROM Student WHERE id = 10000000")
        now_pass = cursor.fetchone()[0]
        self.assertEqual(now_pass, 'abc')

    def test_faculty_right(self):
        db = ConnSQL().conn()
        cursor = db.cursor()
        changer = ChangePass(40000000, 'Faculty', 'yue_pass', 'abc')
        self.assertEqual(changer.change_pass(), "password changed")

        cursor.execute("SELECT password FROM Faculty WHERE id = 40000000")
        now_pass = cursor.fetchone()[0]
        self.assertEqual(now_pass, 'abc')

if __name__ == '__main__':
    unittest.main()

