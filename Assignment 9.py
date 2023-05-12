#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: September 18, 2019
#This program prints out the ASCII code of each character in the phrase
    
word = input("Enter a message:")
codedWord = ""
for ch in word:
	offset = ord(ch) - ord('a') + 13 #how many letters past 'a'
	wrap = offset % 26  #if larger than 26, wrap back to 0
	newChar = chr(ord('a') + wrap)  #compute the new letter
	print(wrap, chr(ord('a') + wrap))    #print the wrap & new letter
	codedWord = codedWord + newChar #add the newChar to the coded word
	    
	print("The coded word (with wrap) is", codedWord)