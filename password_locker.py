from random import random


class Password:
    """
    Here is where we will use to create the paswords
    """
    password_list = []  # list to store user  passwords

    def _init_(self, account, username, password):
        """
        This function will allow the user to create instances of the class with unique details in each instance
        """
        self.account = account
        self.username = username
        self.password = password

    def save_password(self):
        """
        This function will add users password to the password array
        """
        password.password_locker.append(self)

    @classmethod
    def display_passwords(cls):
        """
        This function returns all passwords on the list
        """
        return cls.password_list

    @classmethod
    def delete_password(cls, account):
        """
        This function will delete the users password in the list
        Args:
             This is the account of the password the user wants to delete
        """
        for password in cls.password:
            if password.account.lower() == account.lower():
                cls.password_list.remove(password)

    @classmethod
    def password_exist(cls, account):
        """
        This function checks weather the password of the account exist
        Args:
             acc- this is the acount which user wants to conferm if its password exist
        return:
               True or False
        """
        for password in cls.password_list:
            if password.account.lower() == account.lower():
                return True

                return False