import unittest
from app.models import Blog

class TestUser(unittest.TestCase):
  '''
    Test Class to test the behaviour of the User class
  '''
  def setUp(self):
    self.new_blog = Blog('Coding', 'language','content','12.03.2021',4)
  def test_instance(self):
    self.assertTrue(isinstance(self.new_blog,Blog))
