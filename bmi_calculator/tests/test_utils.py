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
        self.assertNotEqual(bmi_cal(20)[0], 'Underweight')
        self.assertNotEqual(bmi_cal(20)[1], 'Malnutrition risk')
        print("Info: Test cases passed for underweight malnutrition")

    def test_normalweight_low(self):
        self.assertTrue(bmi_cal(23.2)[0], 'Normal weight')
        self.assertTrue(bmi_cal(23.2)[1], 'Low risk')
        self.assertNotEqual(bmi_cal(28)[0], 'Normal weight')
        self.assertNotEqual(bmi_cal(28)[1], 'Low risk')
        print("Info: Test cases passed for normalweight low risk")

    def test_overweight_enhanced(self):
        self.assertTrue(bmi_cal(28)[0], 'Overweight')
        self.assertTrue(bmi_cal(28)[1], 'Enhanced risk')
        self.assertNotEqual(bmi_cal(33)[0], 'Overweight')
        self.assertNotEqual(bmi_cal(33)[1], 'Enhanced risk')
        print("Info: Test cases passed for overweight enhanced risk")

    def test_moderatelyobese_medium(self):
        self.assertTrue(bmi_cal(32)[0], 'Moderately obese')
        self.assertTrue(bmi_cal(32)[1], 'Medium risk')
        self.assertNotEqual(bmi_cal(37)[0], 'Moderately obese')
        self.assertNotEqual(bmi_cal(37)[1], 'Medium risk')
        print("Info: Test cases passed for moderatelyobese medium risk")

    def test_severelyobese_high(self):
        self.assertTrue(bmi_cal(39)[0], 'Severely obese')
        self.assertTrue(bmi_cal(39)[1], 'High risk')
        self.assertNotEqual(bmi_cal(41)[0], 'Severely obese')
        self.assertNotEqual(bmi_cal(41)[1], 'High risk')
        print("Info: Test cases passed for esverely obese high risk")

    def test_veryseverelyobese_veryhigh(self):
        self.assertTrue(bmi_cal(56)[0], 'Very severely obese')
        self.assertTrue(bmi_cal(56)[1], 'Very high risk')
        self.assertNotEqual(bmi_cal(32)[0], 'Very severely obese')
        self.assertNotEqual(bmi_cal(32)[1], 'Very high risk')
        print("Info: Test cases passed for veryseverelyobese very high risk")


if __name__ == '__main__':
    unittest.main()
