#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: October 31, 2019


import pandas as pd

csvFile = input('Enter CSV file name: ')
col = input("Enter attribute: ").strip()
tickets = pd.read_csv(csvFile) 

if(col not in tickets.columns):
   print("Entered Attribute Not Found.Exiting.")
   exit(1)

print("The 10 worst offenders are:")
print(tickets[col].value_counts()[:10]) 
