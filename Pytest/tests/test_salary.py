import unittest
from unittest.mock import MagicMock
from app.salary import Salary

class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = Salary(year=2017)
        s.bonus_api = MagicMock(return_value=1)
        s.calculation_salary()
