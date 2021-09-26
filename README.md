# Project Title

Just after the title, introduce your project by describing attractively what the project is about and what is the main problem that inspires you to create this project or what is the main contribution for the potential user of your project.

---

## Technologies

Describe the technologies required to use your project such as programming languages, libraries, frameworks, and operating systems. Be sure to include the specific versions of any critical dependencies that you have used in the stable version of your project.

---

## Installation Guide

In this section, you should include detailed installation notes containing code blocks and screenshots.

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
