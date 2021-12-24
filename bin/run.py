"""
author@joshnarani
"""
import bmi_calculator
import sys
from bmi_calculator.bmi import BmiCalculator
print(sys.argv[1])
df = BmiCalculator().exe_main(sys.argv[1])

print(df)
