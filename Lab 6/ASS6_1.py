'''
Write a class called Password_manager. The class should have a list called old_passwords that
holds all of the user’s past passwords. The last item of the list is the user’s current pass word.
There should be a method called get_password that returns the current password and a method
called set_password that sets the user’s password. The set_password method should only
change the password if the attempted password is different from all the user’s past passwords.
Finally, create a method called is_correct that receives a string and returns a boolean True or
False depending on whether the string is equal to the current password or not.
'''

class Password_manager:
    def __init__(self):
        self.old_passwords = []
    def get_password(self):
        return self.old_passwords[-1]
    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True  
        return False 
    def is_correct(self,password):
        return password == self.get_password()
passw = Password_manager()
while True:
    print("1. Set a new password")
    print("2. Check current password")
    print("3. Verify a password")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        new = input("Enter a new password: ")
        if passw.set_password(new):
            print("Password set successfully!")
        else:
            print("Password already used. Try a different one.")
    elif choice == "2":
        current = passw.get_password()
        if current:
            print(f"Current password: {current}")
        else:
            print("No password set yet.")
    elif choice == "3":
        password = input("Enter password to verify: ")
        if passw.is_correct(password):
            print("Password is correct.")
        else:
            print("Incorrect password.")
    elif choice == "4":
        print("Exiting Password Manager.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
