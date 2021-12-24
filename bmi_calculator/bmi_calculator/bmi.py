"""
author@joshnarani
"""

import pandas as pd


def exe_main(args):
    if args:
        if type(args) == list:
            """if list of json objects passed"""
            df_data = pd.DataFrame(args)
        else:
            """ if single json object is passed"""
            df_data = pd.DataFrame([args])
        df_data['HeightCm'] = df_data['HeightCm'] / 100
        df_data['HeightCm'] = df_data['HeightCm'].apply(lambda x: x * x)
        df_data['BMI'] = df_data['WeightKg'] / df_data['HeightCm']
        df_data['BMI Category'] = df_data['BMI'].apply(lambda x: bmi_cal(x)[0])
        df_data['Health risk'] = df_data['BMI'].apply(lambda x: bmi_cal(x)[1])
        print(df_data.head)
        return df_data
    else:
        df_data = pd.DataFrame()
        return df_data


def bmi_cal(val: float) -> tuple[str, str]:
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


if __name__ == '__main__':
    import sys

    exe_main(sys.argv[1])
