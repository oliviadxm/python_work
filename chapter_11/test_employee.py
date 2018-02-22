import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Eleanor', 'Park', '105000')

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual('110000', self.employee.salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual('115000', self.employee.salary)


if __name__ == '__main__':
    unittest.main()