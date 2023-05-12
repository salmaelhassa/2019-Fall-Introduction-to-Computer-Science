#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: September 24, 2019
#This program makes a map

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
           floodMap[row,col,2] = 1.0     

        elif elevations[row,col] > 6 and elevations[row,col] <= 20:
           floodMap[row,col,2] = 0.5 
           floodMap[row,col,0] = 0.5 
           floodMap[row,col,1] = 0.5 
        
        elif elevations[row,col] <= 20:
           floodMap[row,col,0] = 1.0  
           
        else:
           floodMap[row,col,1] = 1.0  #Set the green channel to 50%


plt.imsave('floodMap.png', floodMap)
 
