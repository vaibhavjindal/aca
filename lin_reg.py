import numpy as np 


my_data = np.genfromtxt('train_1.csv', delimiter=',')
print my_data.shape
print my_data.dtype.name