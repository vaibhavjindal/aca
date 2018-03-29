import numpy as np 

data_1 = np.genfromtxt('train_1.csv', delimiter=',')#original csv
one_arr=np.ones((100000,1))

#data_2's first column is all ones
data_2=np.append(one_arr,data_1, axis=1)
data_2=np.delete(data_2,101,1)


#y_i is the column vector of y's 
y_i=np.full((100000,1),1,dtype="float64")
for i in range(100000):
	y_i[i][0]=data_1[i][100]

#weights
weights=np.full((101,1),25,dtype="float_")

#loop for number of iterations on the training set
for i in range(10):
	cost=np.full((1,1),0,dtype="float64")
	for j in range(100000):
		err= np.matmul(data_2[j],weights)-y_i[j]
		#cost=cost+np.matmul(err,err)
		for y in range(101):
			weights[y][0]= weights[y][0]-0.0000000000001*(err[0]*data_2[j][y])
	print i
print weights
