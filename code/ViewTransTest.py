import unittest
from ViewTranscript import ViewTranscript

class ViewTransTest(unittest.TestCase):
    def test_exist(self):
        viewer = ViewTranscript(10000000)
        self.assertEqual(viewer.view_trans(), [('CAPP_30300', 'A'), ('MPCS_55001', 'A')])

    def test_no(self):
        viewer = ViewTranscript(60000000)
        self.assertEqual(viewer.view_trans(), [])

if __name__ == '__main__':
    unittest.main()

