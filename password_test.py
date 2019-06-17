import unittest  # importing unittest module
from password_locker import Password  # importing password class


class TestPassword(unittest.TestCase):
    """
    Here is where we will perfome all our test
    """

    def setUp(self):
        """
        This function will create a new instance password before each test
        """
        self.new_password = Password("slack", "Mutai", "0719")

    def tearDown(self):
        """
        Here will be clearing password after every test to avoid confusion
        """
        Password.password = []

    def test_new_pass(self):
        """
        Here will test if a new password is initiated correctly
        """
        self.assertEquall(self.new_password.account, "slack")
        self.assertEquall(self.new_password.username, "Mutai")
        self.assertEquall(self.new_password.password, "0719")

    def test_save_new_password(self):
        """
        Here it will check weather the new password is added in the list
        """
        self.new_password.save_password()
        self.assertEquall(len(Password.paswords), 1)

    def test_add_generate_password(self):
        """
        This will check if the new password added to the list
        """
        new_password = Password("facebook", "6980", Password.generate_(6))
        new_password.save_password()
        self.assertEquall(len(Password.password))

    def test_display_password(self):
        """
        Here it checks weather the display_Password function will return the password in the password list
        """
        self.new_password.test_save_new_password()
        new_pass = Password("facebook", "6980", Password.generate_pass(6))
        new_pass.save_pass()
        self.assertEqual(len(Password.passwords),
                         len(Password.display_passwords()))

    def test_delete(self):
        """
        This test will check whether the password gets deleted from the passwords list
        """
        self.new_password.save_password()
        new_password = Password(
            "facebook", "6980", Password.generate_password(8))
        new_password.save_password()
        Password.delete_password("instagram")
        self.assertEquall(len(Password.password), 1)

    def test_password_exist(self):
        """
        This will check whether the password_exists function works
        """
        self.new_password.save_password()
        self.assertTrue(Password.password_exist("instagram"))

    
