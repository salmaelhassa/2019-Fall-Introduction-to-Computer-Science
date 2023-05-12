#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: October 21, 2019


import csv

print("Enter borough: ")
borough = input()

if borough == "Manhattan":
    index = 1
elif borough == "Brooklyn":
    index = 2
elif borough == "Queens":
    index = 3
elif borough == "Bronx":
    index = 4
elif borough == "Staten Island":
    index = 5

total_pop = 0
population = []

with open('nycHistPop.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    i = 0
    counter = 0
   
    for row in readCSV:
        if i > 5:
            population.append(int(row[index]))
            total_pop = total_pop + int(row[index])
            counter = counter + 1
        i = i + 1
average_pop = total_pop / counter 

max_pop = None
for value in population:
    if not max_pop:
        max_pop = value
    elif value > max_pop:
        max_pop = value
        
min_pop = None
for value in population:
    if not min_pop:
        min_pop = value
    elif value < min_pop:
        min_pop = value
        
print("Minimum Population: " + str(min_pop))        
print("Avearage Population: " + str(average_pop))
print("Maximum Population: " + str(max_pop))