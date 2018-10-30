#import os
#os.chdir("/Users/raul.hennings/Dropbox/Bootcamp_UCBext/Homework-3")
# Import Dependencies
import pandas as pd
import numpy as np

# Create a reference to the CSV and import it into a Pandas DataFrame
csv_path = "./02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv"
PyBank_df = pd.read_csv(csv_path)

Total_Months = len(PyBank_df.index)
Total_Net = PyBank_df['Profit/Losses'].sum()

Diff_PyBank = []
i=1
total = len(PyBank_df['Profit/Losses'])

while i < total:
    Diff = PyBank_df['Profit/Losses'].iloc[int(i)]-PyBank_df['Profit/Losses'].iloc[i-1]
    Diff_PyBank.append(Diff)
    i+=1

Average_Diff = sum(Diff_PyBank)/len(Diff_PyBank)    
Greatest_increase = PyBank_df['Date'].iloc[Diff_PyBank.index(max(Diff_PyBank))+1]
Greatest_decrease = PyBank_df['Date'].iloc[Diff_PyBank.index(min(Diff_PyBank))+1]

print(f'Financial Analysis')
print(f'-------------------------------------')
print(f'Total number months is: {Total_Months}')
print(f'Total: ${Total_Net}')
print(f'Average Change: {Average_Diff}')
print(f'Greatest Incresae in Profits: {Greatest_increase} (${max(Diff_PyBank)})')
print(f'Greatest Decrease in Profits: {Greatest_decrease} (${min(Diff_PyBank)})')

#text_file = open("~/FinancialAnalysis.txt", "w")
with open("FinancialAnalysis.txt", "w") as text_file:
    print(f'Financial Analysis', file=text_file)
    print(f'-------------------------------------', file=text_file)
    print(f'Total number months is: {Total_Months}', file=text_file)
    print(f'Total: ${Total_Net}', file=text_file)
    print(f'Average Change: {Average_Diff}', file=text_file)
    print(f'Greatest Incresae in Profits: {Greatest_increase} (${max(Diff_PyBank)})', file=text_file)
    print(f'Greatest Decrease in Profits: {Greatest_decrease} (${min(Diff_PyBank)})', file=text_file)

text_file.close()
