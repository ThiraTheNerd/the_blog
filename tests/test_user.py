import unittest
from app.models import User

class TestUser(unittest.TestCase):
  '''
    Test Class to test the behaviour of the User class
  '''
  def setUp(self):
    self.new_user = User(1234,'Mercy','thira@gmail.com','my user bio','photos/image.jpg','secretpass',4)
  def test_instance(self):
    self.assertTrue(isinstance(self.new_user,User))
  def test_password_setter(self):
    self.assertTrue(self.new_user.pass_secure is not None)
  def test_no_password_access(self):
    with self.assertTrue(AttributeError):
      self.new_user.pass_secure
  def test_password_verification(self):
    self.assertTrue(self.new_user.verify_password('secretpass'))
