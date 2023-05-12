#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: September 19, 2019
#This program propmts the user for a DNA string


DNA = input("Enter a DNA fragment :")
print(DNA)

l = len(DNA)
print("The length is", l)

numC = DNA.count('C')
numG = DNA.count('G')

gc = (numC + numG) / l

print('GC-content is', gc)

