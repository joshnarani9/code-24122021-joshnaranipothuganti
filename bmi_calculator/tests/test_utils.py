"""
author@joshnarani
"""

import os
import sys
import unittest
from bmi_calculator import bmi_cal

sys.path.append(os.path.abspath('.'))


class Testmodels(unittest.TestCase):

    def test_underweight_malnutrition(self):
        self.assertTrue(bmi_cal(16)[0], 'Underweight')
        self.assertTrue(bmi_cal(16)[1], 'Malnutrition risk')

        print("Info: Test cases passed for underweight malnutrition")

    def test_normalweight_low(self):
        self.assertTrue(bmi_cal(23.2)[0], 'Normal weight')
        self.assertTrue(bmi_cal(23.2)[1], 'Low risk')

        print("Info: Test cases passed for normalweight low risk")

    def test_overweight_enhanced(self):
        self.assertTrue(bmi_cal(28)[0], 'Overweight')
        self.assertTrue(bmi_cal(28)[1], 'Enhanced risk')

        print("Info: Test cases passed for overweight enhanced risk")

    def test_moderatelyobese_medium(self):
        self.assertTrue(bmi_cal(32)[0], 'Moderately obese')
        self.assertTrue(bmi_cal(32)[1], 'Medium risk')

        print("Info: Test cases passed for moderatelyobese medium risk")

    def test_severelyobese_high(self):
        self.assertTrue(bmi_cal(39)[0], 'Severely obese')
        self.assertTrue(bmi_cal(39)[1], 'High risk')

        print("Info: Test cases passed for esverely obese high risk")

    def test_veryseverelyobese_veryhigh(self):
        self.assertTrue(bmi_cal(56)[0], 'Very severely obese')
        self.assertTrue(bmi_cal(56)[1], 'Very high risk')

        print("Info: Test cases passed for veryseverelyobese very high risk")


if __name__ == '__main__':
    unittest.main()
