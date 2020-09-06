import unittest
from accounts import Credentials


class TestCredentials(unittest.TestCase):
    "class that runs the test cases for credentials"

    def setUp(self):
        """
        function that provides default values for the test cases
        """

        self.new_user_credentials = Credentials('facebook', 'lennyk', 'lk1243')

    # 1st test- correct initialization
    def test_init(self):

        self.assertEqual(self.new_user_credentials.acc_name, 'facebook')
        self.assertEqual(self.new_user_credentials.acc_username, 'lennyk')
        self.assertEqual(self.new_user_credentials.acc_password, 'lk1243')

    # 2nd test - to check if created user credentials are being appended
    def test_save_credentials(self):
        """
        checks is new credentials are being appended to the list
        """
        self.new_user_credentials.save_existing_acc()
        self.assertEqual(len(Credentials.user_credential_list), 1)


if __name__ == '__main__':
    unittest.main()
