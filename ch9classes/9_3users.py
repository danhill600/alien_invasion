#9-3. Users: Make a class called User . Create two attributes called first_name
#and last_name , and then create several other attributes that are typically stored
#in a user profile. Make a method called describe_user() that prints a summary
#of the user’s information. Make another method called greet_user() that prints
#a personalized greeting to the user.
#Create several instances representing different users, and call both methods
#for each user.

class Users():
    """a class to keep track of some users"""
    def __init__(self, first, last, email, membership):
        self.first_name = first
        self.last_name = last
        self.email1 = email
        self.membership_type = membership

    def describe_user(self):
        print("User Description:\n" +
              self.first_name + "\n" +
              self.last_name + "\n" +
              self.email1 + "\n" +
              self.membership_type + "\n")
    def greet_user(self):
        print("Greetings, " + self.first_name.title() + " " +
              self.last_name.title() + "!")

user1 = Users('dan', 'hill', 'dhill@witsquash.com', 'nb-individual')
user2 = Users('mariam', 'asad', 'miss.asad@gmail.com', 'nb-individual')
user3 = Users('carlos', 'santana', 'carlos@funtown.biz', 'ultra-premium')

user1.greet_user()
user2.greet_user()
user3.greet_user()
print("-----------")
user1.describe_user()
user2.describe_user()
user3.describe_user()

