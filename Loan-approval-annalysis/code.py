# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here

# loading and reading data
bank = pd.read_csv(path)

# checking the datatype of cloumns
categorical_var = bank.select_dtypes(include='object')
numerical_var = bank.select_dtypes(include='number')

print(categorical_var)
print(numerical_var)




# code ends here


# --------------
# code starts here

banks = bank.drop('Loan_ID', axis=1)


# Checking all missing values
print(banks.isnull().sum())

# apply mode to dataframe
bank_mode = banks.mode().to_dict(orient='records')

# Filling in the missing values
banks.fillna(bank_mode[0], inplace=True)

# Rechecking the missing values
print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here
# creating the pivot table
avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc=np.mean)


print(avg_loan_amount)



# code ends here



# --------------
# code starts here
# calculating percentage of loans approved for self employed and non self employed

loan_approved_se = len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status'] == 'Y')])

loan_approved_nse = len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status'] == 'Y')])

percentage_se = loan_approved_se/614*100
percentage_nse = loan_approved_nse/614*100


# code ends here


# --------------
# code starts here

# Transform the loan tenure from months to years for big audit
months_to_years = lambda x: int(x//12)
loan_term = banks['Loan_Amount_Term'].apply(months_to_years)
big_loan_term = len(loan_term[loan_term >=25])




# code ends here


# --------------
# code starts here

# Income/ Credit History vs Loan Amount
loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()



# code ends here


