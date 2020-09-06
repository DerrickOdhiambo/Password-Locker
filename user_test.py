import unittest
from user import User


class TestUser(unittest.TestCase):
    """class that defines test cases for the user class"""

    def setUp(self):
        """
        defines instructions that would be executed before each test cases
        """
        self.new_user = User(
            'Derrick Odhiambo', 'namteroh', 'test123')

    # 1st test
    def test_init(self):
        """
        Test if the object has been initialized corretly
        """

        self.assertEqual(self.new_user.fullname, 'Derrick Odhiambo')
        self.assertEqual(self.new_user.username, 'namteroh')
        self.assertEqual(self.new_user.password, 'test123')

    # 2nd test if the user details are saved
    def test_save_user(self):
        """
        function to see if the new user credentials are being appended into the list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_credentials), 1)


if __name__ == '__main__':
    unittest.main()
