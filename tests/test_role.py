import unittest
from app.models import Role

class TestUser(unittest.TestCase):
  '''
    Test Class to test the behaviour of the User class
  '''
  def setUp(self):
    self.new_role = Role(name = 'Writer')
