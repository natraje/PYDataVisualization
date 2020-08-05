'''
Created on Dec 26, 2019

@author: natra
'''
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(1,4,100)
y=np.log(x)

plt.figure(1)
plt.subplot(121)
plt.plot(x,y)
plt.xlabel('Values')
plt.ylabel('Log Values')
plt.title('Logger:y=log(x')
plt.show()
plt.subplot(122)
plt.plot(x,y**2)
plt.xlabel('Values')
plt.ylabel('Log Values')
plt.title('Logger:y=y**2')
plt.show()