#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: September 24, 2019
#This program asks user for a name of an image .png file


import matplotlib.pyplot as plt
import numpy as np

colored=input('Enter name of the input file: ')
blue=input('Enter name of the output file: ')

img = plt.imread(colored)   
                       

img2 = img.copy()        
img2[:,:,0] = 0        
img2[:,:,1] = 0         


plt.imsave(blue, img2)  
