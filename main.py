import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

import statsmodels.formula.api as smf
import sys, os


def main():
    csv_path=sys.argv[1]
    ORIGINAL = pd.read_csv(csv_path)
    df = ORIGINAL.copy()
    VARS_REQUIRED = [
        'ConvertedSalary',
        'JobSatisfaction',
        'CareerSatisfaction',
        'SexualOrientation',
        'DevType',
        'EducationTypes',
        'YearsCoding',
        'YearsCodingProf',
        'Gender'
    ]
    df_filter_country = df[(df['Country'] == 'Netherlands') | (df['Country'] == 'Germany')]
    df_filter_employ = df_filter_country[(df_filter_country['Employment'] == 'Employed full-time')]
    df_filter_sex = df_filter_employ[(df_filter_employ['Gender'] == 'Male') | (df_filter_employ['Gender'] == 'Female')]
    df_filter_salary = df_filter_sex[VARS_REQUIRED]
    list(df_filter_salary.JobSatisfaction.unique())
    df_filter_salary = df_filter_salary[(df_filter_salary['Gender'].notnull()) & (df_filter_salary['SexualOrientation'].notnull()) & (df_filter_salary['JobSatisfaction'].notnull())]
    df_filter_salary['JobSatisfaction'] = df_filter_salary['JobSatisfaction'].replace({
        'Extremely dissatisfied': 0,
        'Moderately dissatisfied': 1,
        'Slightly dissatisfied': 2,
        'Neither satisfied nor dissatisfied': 3,
        'Slightly satisfied': 4,
        'Moderately satisfied': 5,
        'Extremely satisfied': 6
    })
    
    # clean up np.NaN values
    df_filter_salary['GenderBinary'] = np.where((df_filter_salary['Gender'] == 'Male'), 1, 0)
    df_filter_salary['OrientationBinary'] = np.where((df_filter_salary['SexualOrientation'] == 'Straight or heterosexual'), 'OrientConforming', 'OrientNonConforming')
    filtered = df_filter_salary.copy()
    #filtered = pd.concat([filtered, pd.get_dummies(filtered['GenderBinary'])], axis=1)
    filtered = pd.concat([filtered, pd.get_dummies(filtered['OrientationBinary'])], axis=1)
    #filtered = pd.concat([filtered, pd.get_dummies(filtered['Gender'])], axis=1)
    filtered = pd.concat([filtered, pd.get_dummies(filtered['SexualOrientation'])], axis=1)
    final_df = filtered[['ConvertedSalary', 'OrientationBinary', 'YearsCodingProf', 'GenderBinary', 'JobSatisfaction']]
    results1 = smf.ols('ConvertedSalary ~ OrientationBinary + YearsCodingProf + GenderBinary', data=final_df).fit()
    results1.summary()
    results2 = smf.ols('JobSatisfaction ~ OrientationBinary + YearsCodingProf + GenderBinary', data=final_df).fit()
    results2.summary()
    # DevType
    # EducationTypes
    # Gender
    # Orientation
    uniques = []
    columns = ['DevType', 'EducationTypes', 'Gender', 'SexualOrientation']
    for col in columns:
        options = filtered[col]
        options = options.replace(np.nan, 'n/a')
        for s in options:
            if s.find(';'):
                split = s.split(';')
                for _s in split:
                    if _s not in uniques:
                        uniques.append(_s)
            else:
                if s not in uniques:
                    uniques.append(s)
    uniques
    df.Gender.unique()


main()