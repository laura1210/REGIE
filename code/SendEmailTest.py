import unittest
from SendEmail import SendEmail

class SendEmailTest(unittest.TestCase):
    def test_right(self):
        sender = SendEmail(10000000,'MPCS_51410','Hello','Welcome to the course')
        self.assertEqual(sender.send_email(), ['laura@uchicago.edu',
                                               'tony@uchicago.edu',
                                               'steph@uchicago.edu',
                                               'jane@uchicago.edu'])

    def test_wrong(self):
        sender = SendEmail(20000000,'MPCS_51410','Hello','Welcome to the course')
        self.assertEqual(sender.send_email(), [])

if __name__ == '__main__':
    unittest.main()

