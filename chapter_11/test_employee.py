import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee('kato', 'luo', 200000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(205000, self.my_employee.wage)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(210000, self.my_employee.wage)

unittest.main()