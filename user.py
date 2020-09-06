class User:
    """
    User class for creating password locker account and logging in
    """

    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_user(self):
        """
        a funtion for saving user credentials after creating a account
        """
        User.user_details.append(self)
