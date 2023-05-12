#Name: Salma Elhassa
#Email: salma.elhassa52@myhunter.cuny.edu
#Date: September 24, 2019
#This program makes a C logo

import matplotlib.pyplot as plt 
import numpy as np 
logoImg = np.ones((30,30,3)) 

logoImg[:,:10,0] = 0 
logoImg[:,:10,1] = 0

logoImg[0:10,:,0] = 0 
logoImg[0:10,:,1] = 0

logoImg[20:30,:,0] = 0 
logoImg[20:30,:,1] = 0


plt.imsave("logo.png", logoImg) 

