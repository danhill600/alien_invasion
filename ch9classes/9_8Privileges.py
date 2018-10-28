#9-8. Privileges: Write a separate Privileges class. The class should have one
#attribute, privileges , that stores a list of strings as described in Exercise 9-7.
#Move the show_privileges() method to this class. Make a Privileges instance
#as an attribute in the Admin class. Create a new instance of Admin and use your
#method to show its privileges.

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

class Privileges()
    """A simple attempt to model privileges for a user"""
    def __init __(self)
    self.privileges = ["can edit", "can post", "can copy"]

class Admin(User):
    """An attempt to model an Admin"""

    def __init__(self, first_name, last_name, email, membership, employer):
        super().__init__(first_name, last_name, email, membership,
                         employer)
        adprivies = Privileges( 

user1 = User('Ah', 'Clem', 'ahclem@bozos.fun', 'nb-individual', 'funland')
user2 = User('Count', 'Dracula', 'fangs@monsters.biz', 'sponsor', 'castle')

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

superuser = Admin("Dan", "Hill", "derbs@funeral.dirge", "nb-individual", "ABC")
superuser.show_privilages()
