class Credentials:
    """
    a class for user accounts and account details
    """
    user_credential_list = []

    def __init__(self, acc_name, acc_username, acc_password):
        self.acc_name = acc_name
        self.acc_username = acc_username
        self.acc_password = acc_password

    def save_existing_acc(self):
        """
        function to save existing user credentials
        """
        Credentials.user_credential_list.append(self)
