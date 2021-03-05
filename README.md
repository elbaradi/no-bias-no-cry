# no-bias-no-cry
Qing, Jesse, Pavel and Tijmen's project for Codam's 'Hack The Bias' 2021 hackathon.

## Project description

For this project we were looking for biases in a dataset provided by Mega-Inc. Our
analysis looks at hetero and non-hetersexual Males and Females and checks for trends
regarding ConvertedSalary and JobSatisfaction.

## Contents

This repository contains notebooks used for analysing the data provided. *analysis.ipynb* file
contains raw plots and tables but nothing concrete. The *cleanup.ipynb* file contains more
structured code building up to two ols models being fitted and summarised.

The *main.py* file essentially runs the *cleanup.ipynb* its code. The data file can be passed
through the command line too the program, which will spit out two OLS summaries.
