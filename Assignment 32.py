#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: October 28, 2019


import pandas as pd
import matplotlib.pyplot as plt

input_file_name = input("Enter the input file name ")

output_file_name = input("Enter the file name ")

data = pd.read_csv(input_file_name)

child_data = data['Fraction Children']

plt.plot(data['Date of census'],child_data,label='Fraction Children')
plt.legend()
plt.xlabel("Date of Census")
plt.savefig(output_file_name)

