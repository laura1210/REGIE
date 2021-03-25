import unittest
from ConnSQL import ConnSQL
from AssignGrade import AssignGrade

class AssignGradeTest(unittest.TestCase):

    def tearDown(self):
        # change back to original database
        db = ConnSQL().conn()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Grade WHERE course_code = 'MPCS_51410'")
        db.commit()

    def test_wrong(self):
        db = ConnSQL().conn()
        cursor = db.cursor()
        grader = AssignGrade(30000000, 'MPCS_51410', 10000000, 'A')
        self.assertEqual(grader.assign_grade(), "you don't teach this course")

    def test_new(self):
        db = ConnSQL().conn()
        cursor = db.cursor()
        grader = AssignGrade(10000000, 'MPCS_51410', 10000000, 'B')
        self.assertEqual(grader.assign_grade(), "assign grade successfully")

        cursor.execute("SELECT grade FROM Grade WHERE student_id=10000000 AND course_code='MPCS_51410'")
        now_grade = cursor.fetchone()[0]
        self.assertEqual(now_grade, 'B')

    def test_exist(self):
        db = ConnSQL().conn()
        cursor = db.cursor()
        grader = AssignGrade(10000000, 'MPCS_51410', 10000000, 'A')
        self.assertEqual(grader.assign_grade(), "assign grade successfully")

        cursor.execute("SELECT grade FROM Grade WHERE student_id=10000000 AND course_code='MPCS_51410'")
        now_grade = cursor.fetchone()[0]
        self.assertEqual(now_grade, 'A')

if __name__ == '__main__':
    unittest.main()

