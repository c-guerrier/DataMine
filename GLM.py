# Import packages:

import pandas as pd
import numpy as np
import statsmodels.api as sm


## AIM1:
    ## ED visits due to diabetes are higher in counties with higher proportion of low-income people.
    ## ED visits due to diabetes are higher in counties with lower proportion of educated people.

# Read the data and display it
main = pd.read_csv("Dataset_Main.csv", encoding="utf-8", encoding_errors="ignore")

# Fit a logistic regression model in order to predict 'ED_Visits_Diabetes' using following covariates
    # 'Percentage_Population_Black'
    # 'Median_household_income'
    # 'Renter'
    # 'No_HS'
    # 'Park'
    # 'Fast_food'
    # 'Overweight'
    # 'Sedentary'
    # 'Medical_checkup'
    # 'Food_insecurity'

# We'll build our model using the `glm()` function, which is part of the formula submodule of (statsmodels)

import statsmodels.formula.api as smf

# We can use a formula string to separate the predictors from the response.

main_formula = 'ED_Visits_Diabetes ~ Percentage_Population_Black+Median_household_income+Renter+No_HS+Park+Fast_food+Overweight+Sedentary+Medical_checkup+Food_insecurity'

main_model = smf.glm(formula = main_formula, data=main)
main_result = main_model.fit()
print(main_result.summary())

# Read the data and display it
sub_white = pd.read_csv("Dataset_Sub_White.csv", encoding="utf-8", encoding_errors="ignore")

# Fit a logistic regression model in order to predict 'ED_Visits_Diabetes' using following covariates
    # 'Percentage_Population_White'
    # 'Median_household_income'
    # 'Renter'
    # 'No_HS'
    # 'Overweight'
    # 'Sedentary'
    # 'Medical_checkup'

# We'll build our model using the `glm()` function, which is part of the formula submodule of (statsmodels)

import statsmodels.formula.api as smf

# We can use a formula string to separate the predictors from the response.

sub_formula_w = 'ED_Visits_Diabetes ~ Percentage_Population_White+Median_household_income+Renter+No_HS+Overweight+Sedentary+Medical_checkup'

sub_model_w = smf.glm(formula = sub_formula_w, data=sub_white)
sub_result_w = sub_model_w.fit()
print(sub_result_w.summary())


# Read the data and display it
sub_white = pd.read_csv("Dataset_Sub_White.csv", encoding="utf-8", encoding_errors="ignore")

# Fit a logistic regression model in order to predict 'ED_Visits_Diabetes' using following covariates
    # 'Percentage_Population_White'
    # 'Median_household_income'
    # 'Renter'
    # 'No_HS'
    # 'Overweight'
    # 'Sedentary'
    # 'Medical_checkup'

# We'll build our model using the `glm()` function, which is part of the formula submodule of (statsmodels)

import statsmodels.formula.api as smf

# We can use a formula string to separate the predictors from the response.

sub_formula_w = 'ED_Visits_Diabetes ~ Percentage_Population_White+Median_household_income+Renter+No_HS+Overweight+Sedentary+Medical_checkup'

sub_model_w = smf.glm(formula = sub_formula_w, data=sub_white)
sub_result_w = sub_model_w.fit()
print(sub_result_w.summary())


# Read the data and display it
sub_black = pd.read_csv("Dataset_Sub_Black.csv", encoding="utf-8", encoding_errors="ignore")

# Fit a logistic regression model in order to predict 'ED_Visits_Diabetes' using following covariates
    # 'Percentage_Population_Black'
    # 'Median_household_income'
    # 'Renter'
    # 'No_HS'
    # 'Overweight'
    # 'Sedentary'
    # 'Medical_checkup'

# We'll build our model using the `glm()` function, which is part of the formula submodule of (statsmodels)

import statsmodels.formula.api as smf

# We can use a formula string to separate the predictors from the response.

formula = 'ED_Visits_Diabetes ~ Percentage_Population_Black+Median_household_income+Renter+No_HS+Overweight+Sedentary+Medical_checkup'

sub_model_b = smf.glm(formula = formula, data=sub_black)
sub_result_b = sub_model_b.fit()
print(sub_result_b.summary())
