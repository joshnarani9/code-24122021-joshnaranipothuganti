"""
author@joshnarani
"""
import json

import numpy as np
import pandas as pd
from bmi_calculator import divide, bmi_cal


def bmi_data(json_inp):
    if type(json_inp) == list:
        """if list of json objects passed"""
        df_data = pd.DataFrame(json_inp)
    else:
        print(type(json_inp))
        """ if single json object is passed"""
        df_data = pd.DataFrame([json_inp])
    df_data['HeightCm'] = df_data['HeightCm'].astype(float)
    df_data['WeightKg'] = df_data['WeightKg'].astype(float)
    df_data['HeightCm'] = df_data['HeightCm'] / 100
    df_data['BMI'] = np.vectorize(divide)(df_data['WeightKg'], (df_data['HeightCm']).pow(2))
    df_data['BMI Category'] = df_data['BMI'].apply(lambda x: bmi_cal(x)[0])
    df_data['Health risk'] = df_data['BMI'].apply(lambda x: bmi_cal(x)[1])
    df_data['cat&risk'] = df_data['BMI Category'] + '_' + df_data['Health risk']
    df = df_data['cat&risk'].value_counts().rename_axis('cat_and_risk').reset_index(name='counts')
    df = dict(zip(df['cat_and_risk'], df['counts']))
    print("Info: Successfully found count of all category_with_riskfactor")
    print("Info: output count is...")
    print(df)

    return df


class BmiCalculator:

    def exe_main(self, file: str):
        if file:
            """ args is filepath with json input data"""
            with open(file, 'r') as content:
                json_inp = json.load(content)
            print(type(json_inp))
            df = bmi_data(json_inp)
        else:
            """args here passed is json object"""
            print("Info: Input file path is not provided")
            df = None
        return df

# if __name__ == '__main__':
#     import sys
#
#     ob = BmiCalculator().exe_main(sys.argv[1])
