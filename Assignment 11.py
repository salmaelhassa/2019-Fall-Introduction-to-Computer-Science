#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: September 20, 2019
#This program propmts the user for a DNA string



templateString = "If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN."

noun = input("Enter a noun: ")
templateString = templateString.replace("NOUN", noun)
verb1 = input("Enter a verb: ")
templateString = templateString.replace("VERB1", verb1)
verb2 = input("Enter another verb: ")
templateString = templateString.replace("VERB2", verb2)
print("\nNew sentence:\n" + templateString)