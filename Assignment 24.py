#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: October 16, 2019

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

medBlue = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
           b = input('How blue is the ocean? : ')
           medBlue[row,col,2] = b    
           medBlue[row,col,1] = 0       
           medBlue[row, col,0]= 0      
r.cuny        elif elevations[row,col]%10==0:
           medBlue[row,col,0] = 0    
           medBlue[row,col,1] = 0     
           medBlue[row,col,2] = 0      
        else:
           medBlue[row,col,0] = 1.0   
           medBlue[row,col,1] = 1.0  
	   medBlue[row,col,2] = 1.0   

   
plt.imsave('medBlue.png', medBlue)