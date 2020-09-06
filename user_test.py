import unittest
from user import User


class TestUser(unittest.TestCase):
    """class that defines test cases for the user class"""

    def setUp(self):
        """
        defines instructions that would be executed before each test cases
        """
        self.new_user = User(
            'Derrick', 'Odhiambo', 'odhiamboderrick56@gmail.com', 'namteroh', 'test123')

    # 1st test
    def test_init(self):
        """
        Test if the object has been initialized corretly
        """

        self.assertEqual(self.new_user.first_name, 'Derrick')
        self.assertEqual(self.new_user.last_name, 'Odhiambo')
        self.assertEqual(self.new_user.email, 'odhiamboderrick56@gmail.com')
        self.assertEqual(self.new_user.username, 'namteroh')
        self.assertEqual(self.new_user.password, 'test123')


if __name__ == '__main__':
    unittest.main()
