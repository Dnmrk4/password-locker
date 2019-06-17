class User:
   
    def _init_(self,login,password):
      
      self.login = login
      self.password = password

    def user_exist(self,password):
      
      if self.password == password:
    return True