from password_locker import Password
from user import User
import getpass #to hide the pass

def new_user(login,password):

    """
    This will create a new user every time they login
    Args:
        login - user name
        password - the user's password
    Return:
        the new user instance
    """
    user = User(login,password)
    return user

def add_password(account,username,password):
    """
    This is a function that will add a new password to the passwords list
    """
    new_pass = Password(account,username,password)
    new_pass.save_password()

def generate_password(length):
    """
    This will create a random password for the user
    Args:
        length - the user's preferred length for the password
    Return:
        It will return a random password of user's preferred length
    """
    return Password.generate_pass(length)

def view_passwords():
    """
    A function that will allow the user to view all the passwords
    """
    return Password.view_passwords()

def delete_password(acc):
    """
    This is a function that will delete the password
    Args:
        acc - the acc of the pass the user wants to delete
    """
    Password.delete_password(acc)

def password_exists(acc):
    """
    It will check whether a password exists
    Args:
        acc- the password's account
    Return:
        True or False
    """
    return Password.password_exist(acc)

def main():
    """
    This is where the user will run all their functions
    """

    print("\n")
    print("|`````\   /````\   /``````\   /``````\  |`|          |`|  /``````\  |``````\   |`````\      |`|      /``````\    /```````\  |`| /`/  |``````|  |``````\    ")
    print("| |``| | | /``\ | | |````\ | | |````\ | | |          | | | /````\ | | |```| |  | |``\ |     | |     | /````\ |  |  /````\|  | |/ /   | |`````  | |```| |   ")
    print("| |```/  | |  | |  \  ````\   \  ````\   \ \  /``\  / /  | |    | | | |``` /   | |  | |     | |     | |    | |  | |         | | |    | `````|  | |``` /    ")
    print("| |```   | |``| |   `````| |   `````| |   \ \/ /\ \/ /   | \    / | | |````\   | |  / |     | |     | \    / |  |  \    /|  | |\ \   | |`````  | |````\    ")
    print("| |      | |``| |  \````` /   \````` /     \  /  \  /     \ ```` /  | |```\ \  | ``` /      |  ```|  \ ```` /    \  ```` /  | | \ \  | `````|  | |```\ \   ")
    print("```      ```  ```   ``````     ``````       ```   ```      ``````   ```    ``` ``````       ```````   ``````      ``````    ```  ``` ````````  ```    ```  \n")
 

    print("This app was developed by *Danmark Mutai*\n")
    print("Welcome to PASSWORD LOCKER. We help you manage your passwords so that you can worry about things that matter\n")
    print("-"*6,"SIGN UP","-"*6,"\n")

    user_name = input("User Name\n")
    user_pass = getpass.getpass('Password:\n')

    #new_user(login,password)

    print(f"Welcome {user_name}\n")

    print("What would you like to do?\n")

    while True:
        command = input("You can use 'gg' to  generate a password, 'aa' to add an existing password, 'dd' to delete a password, 'vv' to view all your passwords, 'exit' to leave :( \n")
        if command == "aa":
            print("Oh cool. Enter your new passwords\n")
            acc = input("Which platform is the password for?\n")
            user_name = input("What is your username?\n")
            password = getpass.getpass("What is your password?\n")

            add_password(acc,user_name,password)

            print(f"New password for {acc} added\n")
        elif command == "gg":
            print("I like generating password for you!")
            acc = input("Which platform is the password for?\n")
            user_name = input("What is your username?\n")
            length = input("What is the length of the password you would like me to generate, please enter any number\n")
            try:
                add_password(acc,user_name,generate_password(int(length)))
                print(f"New password for {acc} generated\n")
            except ValueError:
                print("Please use numbers only\n")
        elif command == "dd":
            print("Oh no!:(\n")
            pass_word = getpass.getpass("Enter your password?\n")
            if pass_word == user_pass:
                acc= input("Which account would you like to delete their password?\n")
                if password_exists(acc):
                    print(f"{acc} password deleted\n")
                    if delete_password(acc):
                       print(f"{acc} password deleted\n")      
                else:
                    print("Password doesn't exist\n")
            else:
                print("\nOh no. Wrong password. Try Again\n")
        elif command == "vv":
            pass_word = getpass.getpass("Enter your password?\n")
            if pass_word == user_pass:
                if view_passwords():
                    for password in view_passwords():
                        print("-"*6,view_passwords().index(password)+1,"-"*6,"\n")
                        print(f"Account --> {password.account}\n")
                        print(f"Username --> {password.username}\n")
                        print(f"Password --> {password.password}\n")
                else:
                    print("You have no passwords\n")
            else:
                print("Wrong password. You can't view the passwords. Try again\n")
        elif command == "exit":
            print("Please stay:(")
            print("Bye")
            break

if __name__ == "__main__":
    main()