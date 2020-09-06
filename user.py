class User:
    """
    User class for creating password locker account and logging in
    """

    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    user_details = []  # empty user details list

    def save_user(self):
        """
        a funtion for saving user credentials after creating a account
        """
        User.user_details.append(self)