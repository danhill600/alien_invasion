class User():
    """An attempt to model users."""

    def __init__(self,first_name, last_name, email, membership, employer):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.membership = membership
        self.employer = employer

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() +
               " is employed by " + self.employer.title() + ".")

    def greet_user(self):
        print("Always nice to see you again, " + self.first_name.title() +
              " " + self.last_name.title())

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
