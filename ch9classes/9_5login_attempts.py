#9-3. Users: Make a class called User . Create two attributes called first_name
#and last_name , and then create several other attributes that are typically stored
#in a user profile. Make a method called describe_user() that prints a summary
#of the user’s information. Make another method called greet_user() that prints
#a personalized greeting to the user.
#Create several instances representing different users, and call both methods

#9-5. Login Attempts: Add an attribute called login_attempts to your User
#class from Exercise 9-3 (page 166). Write a method called increment_
#login_attempts() that increments the value of login_attempts by 1. Write
#another method called reset_login_attempts() that resets the value of login_
#attempts to 0.
#Make an instance of the User class and call increment_login_attempts()
#several times. Print the value of login_attempts to make sure it was incremented
#properly, and then call reset_login_attempts() . Print login_attempts again to
#make sure it was reset to 0.

class User():
    """An attempt to model users."""

    def __init__(self,first_name, last_name, email, membership, employer):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.membership = membership
        self.employer = employer
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() +
               " is employed by " + self.employer.title() + ".")

    def greet_user(self):
        print("Always nice to see you again, " + self.first_name.title() +
              " " + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Ah', 'Clem', 'ahclem@bozos.fun', 'nb-individual', 'funland')
user2 = User('Count', 'Dracula', 'fangs@monsters.biz', 'sponsor', 'castle')

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(str(user1.login_attempts))
user1.reset_login_attempts()
print(str(user1.login_attempts))
