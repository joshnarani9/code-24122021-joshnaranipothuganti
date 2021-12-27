"""
author@joshnarani
"""
""" Includes utilities required for bmi calculation"""

from typing import Tuple


def divide(a, b):
    if b == 0:
        return 0
    return float(a) / float(b)


def bmi_cal(val: float) -> Tuple[str, str]:
    if val <= 18.4:
        bmi_category = "Underweight"
        health_risk = "Malnutrition risk"
    elif 18.5 <= val <= 24.9:
        bmi_category = "Normal weight"
        health_risk = "Low risk"
    elif 25 <= val <= 29.9:
        bmi_category = "Overweight"
        health_risk = "Enhanced risk"
    elif 30 <= val <= 34.9:
        bmi_category = "Moderately obese"
        health_risk = "Medium risk"
    elif 35 <= val <= 39.9:
        bmi_category = "Severely obese"
        health_risk = "High risk"
    else:
        bmi_category = "Very severely obese"
        health_risk = "Very high risk"
    return bmi_category, health_risk
