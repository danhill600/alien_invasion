#9-7. Admin: An administrator is a special kind of user. Write a class called
#Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
#or Exercise 9-5 (page 171). Add an attribute, privileges , that stores a list
#of strings like "can add post" , "can delete post" , "can ban user" , and so on.

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
class Admin(User):
    """An attempt to model an Admin"""

    def __init__(self, first_name, last_name, email, membership, employer):
        super().__init__(first_name, last_name, email, membership,
                         employer)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privilages(self):
        print(self.privileges)


user1 = User('Ah', 'Clem', 'ahclem@bozos.fun', 'nb-individual', 'funland')
user2 = User('Count', 'Dracula', 'fangs@monsters.biz', 'sponsor', 'castle')

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

superuser = Admin("Dan", "Hill", "derbs@funeral.dirge", "nb-individual", "ABC")
superuser.show_privilages()
