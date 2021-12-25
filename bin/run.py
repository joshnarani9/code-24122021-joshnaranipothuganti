"""
author@joshnarani
"""
import sys
from bmi_calculator.bmi import BmiCalculator

print(sys.argv)
if len(sys.argv) == 3:
    print((sys.argv[1]))
    BmiCalculator().exe_main(sys.argv[1], eval(sys.argv[2]))
else:
    print((sys.argv[1]))
    BmiCalculator().exe_main(sys.argv[1])
