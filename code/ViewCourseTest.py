import unittest
from ViewCourse import ViewCourse

class ViewCourseTest(unittest.TestCase):
    def test_faculty(self):
        viewer = ViewCourse(10000000, 'Faculty')
        self.assertEqual(viewer.view_course(), ['MPCS_51410'])

    def test_student(self):
        viewer = ViewCourse(10000000, 'Student')
        self.assertEqual(viewer.view_course(), ['MPCS_51410','MPCS_52553','PPHA_36800','CAPP_30300','MPCS_55001'])

if __name__ == '__main__':
    unittest.main()

