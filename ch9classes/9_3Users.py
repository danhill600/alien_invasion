#9-3. Users: Make a class called User . Create two attributes called first_name
#and last_name , and then create several other attributes that are typically stored
#in a user profile. Make a method called describe_user() that prints a summary
#of the user’s information. Make another method called greet_user() that prints
#a personalized greeting to the user.
#Create several instances representing different users, and call both methods


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

user1 = User('Ah', 'Clem', 'ahclem@bozos.fun', 'nb-individual', 'funland')
user2 = User('Count', 'Dracula', 'fangs@monsters.biz', 'sponsor', 'castle')

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()
