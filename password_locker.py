from random import random


class Password:
    """
    Here is where we will use to create the paswords
    """
    password_list = []  # list to store user  passwords

    def _init_(self, account, username, password):
        
        self.account = account
        self.username = username
        self.password = password

    def save_password(self):
        
        password.password_locker.append(self)

    @classmethod
    def display_passwords(cls):
        
        return cls.password_list

    @classmethod
    def delete_password(cls, account):
       
        for password in cls.password:
            if password.account.lower() == account.lower():
                cls.password_list.remove(password)

    @classmethod
    def password_exist(cls, account):
        
        for password in cls.password_list:
            if password.account.lower() == account.lower():
                return True

            return False