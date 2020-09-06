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
