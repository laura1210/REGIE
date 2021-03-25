import unittest
from ViewStudent import ViewStudent

class ViewStudentTest(unittest.TestCase):
    def test(self):
        viewer = ViewStudent('MPCS_52553')
        self.assertEqual(viewer.view_student(), [10000000,30000000,50000000])

if __name__ == '__main__':
    unittest.main()

