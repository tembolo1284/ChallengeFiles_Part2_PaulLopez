import csv
from pathlib import Path

def writeToCSV(csvSavePath,qualifying_loans):
    header = ["Lender","Max Loan Amount", "Max LTV,Max DTI", "Min Credit Score", "Interest Rate"]

    #print(qualifying_loans) #Just checking variable value
    #print(csvSavePath) #Just checking variable value
    csvpath = Path(csvSavePath)
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
    
    # Write our header row first!
        csvwriter.writerow(header)
        #Write the rest of the csv by populating with qualifying loans. Thank you google for the syntax
        #https://stackoverflow.com/questions/14037540/writing-a-python-list-of-lists-to-a-csv-file

        wr = csv.writer(csvfile)
        wr.writerows(qualifying_loans)
       
       # for row in qualifying_loans:
       #     csvwriter.writerow(row.values())
        
        print("File has been saved under directory and file: {csvSavePath}.  Have a nice day!")



