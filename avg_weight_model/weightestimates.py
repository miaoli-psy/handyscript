# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:43:52 2023

@author: Miao
"""

from sklearn.linear_model import LinearRegression
import pandas as pd

# read data
data = pd.read_excel("contrast_34sub_miao_sub1.xlsx")

# get unique subject ID
subjects = data['Subject'].unique()

# dictionary to store the estimates
weights_per_subject_congruency = {}


# linear regression
for subject in subjects:
    subject_data = data[data['Subject'] == subject]
    
    # Get congruency conditions for the subject
    congruency_conditions = subject_data['congruency'].unique()
    
    for condition in congruency_conditions:
        
        # diff condi
        condition_data = subject_data[subject_data['congruency'] == condition]

        # define x and y
        X_condition = condition_data[['emotion_fovea', 'emotion_flankers']]
        y_condition = condition_data['SubjectSelected']

        # Fit model
        model_condition = LinearRegression().fit(X_condition, y_condition)

        # Store data
        weights_per_subject_congruency[(subject, condition)] = model_condition.coef_

weights_per_subject_congruency

