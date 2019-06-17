import unittest
from user import User

class TestUser(unittest.TestCase):
   
    def setUp(self):
        
        self.new_user("dnmrk","6980")

    def test_init(self):
        
        self.assertEquall(self.new_user.login,"dnmrk")
        self.assertEquall(self.new_user.password,"6980")

    def test_user_password(self):
        
        self.assertTrue(User.user_exists)

    if __name__ == "__main__":
        unittest.main()        
