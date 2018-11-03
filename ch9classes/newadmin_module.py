"""A module for 9_12"""
from newuser_module import User

class Privileges():
    """A simple attempt to model privileges for a user"""
    def __init__(self):
        self.privileges = ["can edit", "can post", "can copy"]

    def show_privileges(self):
       print(self.privileges)


class Admin(User):
    """An attempt to model an Admin"""

    def __init__(self, first_name, last_name, email, membership, employer):
        super().__init__(first_name, last_name, email, membership, employer)
        self.adprivs = Privileges()
