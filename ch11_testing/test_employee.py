import unittest
from EmployeeModule import Employee

class TestEmployee(unittest.TestCase):
    "Tests for the class Employee"""

    def setUp(self):
        first = 'Dennis'
        last = 'Claplander'
        salary = 50000
        self.my_dude = Employee(first, last, salary)

    def test_give_default_raise(self):
        self.my_dude.give_raise()
        self.assertEqual(self.my_dude.salary, 55000)

    def test_give_custom_raise(self):
        self.my_dude.give_raise(10000)
        self.assertEqual(self.my_dude.salary, 60000)

unittest.main()
