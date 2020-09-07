import unittest
from accounts import Credentials


class TestCredentials(unittest.TestCase):
    "class that runs the test cases for credentials"

    def setUp(self):
        """
        function that provides default values for the test cases
        """

        self.new_user_credentials = Credentials('facebook', 'lennyk', 'lk1243')

    def tearDown(self):
        """funtion that does clean up after each test case"""

        Credentials.user_credential_list = []

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

    # 3rd test
    def test_save_multiple_credenials(self):
        """
        test to see if user can save multiple credentials
        """

        self.new_user_credentials.save_existing_acc()
        test_credentials = Credentials('instagram', 'kravlenny', '123kravs')
        test_credentials.save_existing_acc()
        self.assertEqual(len(Credentials.user_credential_list), 2)

    # 4th test
    def test_display_credentials(self):
        """
        method that returns a list of all saved credentials
        """

        self.assertEqual(Credentials.display_user_credentials(),
                         Credentials.user_credential_list)

    def test_find_credentials(self):
        """
        Test to see if a user can search for a specific account in the application
        """

        self.new_user_credentials.save_existing_acc()
        test_account = Credentials('Facebook', 'derricko', 'fb456')
        test_account.save_existing_acc()

        found_account = Credentials.find_by_username('derricko')
        self.assertEqual(found_account.acc_name, test_account.acc_name)

    def test_delete_credentials(self):
        """
        test to see if user can delete existing credentials
        """

        self.new_user_credentials.save_existing_acc()
        test_credential = Credentials('slack', 'lennyK', 'len1234')
        test_credential.save_existing_acc()

        self.new_user_credentials.delete_user_credentials()
        self.assertEqual(len(Credentials.user_credential_list), 1)


if __name__ == '__main__':
    unittest.main()
