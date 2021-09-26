# Project Title

This is the Loan Qualifier Application for challenge #2! I ask for various inputs from the user, and then 
check to see if he qualifies for the various loans I have available which I upload from a CSV file.

If the user qualifies for loans, I then ask if they would like to save the results to a CSV file. If they say yes,
I have them enter a file and directory and then all the loans they qualified for are saved to this CSV file.

---

## Technologies

I am using python version 3.7.10 and am importing the following from the built-in libraries and from functions i've created myself:
import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import load_csv
from qualifier.utils.writeToCSV import writeToCSV

from qualifier.utils.calculators import (calculate_monthly_debt_ratio,calculate_loan_to_value_ratio,)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value
---

## Installation Guide

I have python version 3.7.10 and git version 2.33.0.windows.2 installed on a laptop running windows 10 pro.

I have VS Code version 1.60.1 installed.


---

## Usage

Only sticking points one might encounter is as it relates to the CSV files.
Run the program as normal with python app.py.  Enter in the values from the questionnaire.
When you are prompted for your first csv file and directory enter ./data/daily_rate_sheet.csv.
After that if you so wish to save out the results of your program make sure you enter
the csv file and directory as ./data/loanResults.csv.

That's it!


---

## Contributors
Just me, Paul Lopez, and the stackoverflow website!


---
## Acceptance Criteria
1) Given that I’m using the loan qualifier CLI, when I run the qualifier, then the tool should prompt the user to save the results as a CSV file. 

I put in code with logic that prompts the user IF there are qualifying loans. Otherwise code exits with a goodbye and thank you message.

2) Given that no qualifying loans exist, when prompting a user to save a file, then the program should notify the user and exit.

I put in logic that exits with a goodbye message if there are 0 qualifying loans.

3) Given that I have a list of qualifying loans, when I’m prompted to save the results, then I should be able to opt out of saving the file. 

I put in logic that asks the user if he wants to save results of questionnaire IF there are qualifying loans.  If they respond no the program thanks them and exits.

4) Given that I have a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file. 

I put in code that prompts user IF he wants to save a file to enter the file path for where the results will be stored.

5) Given that I’m using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file.

I put in code that saves CSV file with hardcoded name "LoanResults.csv" to the directory determined by the user.


---

## License

When you share a project on a repository, especially a public one, it's important to choose the right license to specify what others can and can't with your source code and files. Use this section to include the license you want to use.
