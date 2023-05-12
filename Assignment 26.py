#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: October 18, 2019



import pandas as pd
import matplotlib.pyplot as plt



pop = pd.read_csv('nycHistPop.csv',skiprows=5)

borough = input('Enter borough name:')

pop['Fraction'] = pop[borough]/pop['Total']

image = input('Enter image name:')

pop.plot(x = 'Year' , y = 'Fraction')

plt.savefig(image)