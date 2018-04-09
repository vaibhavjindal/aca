import numpy as np 
import random

#define the 7x7 maze
#0s define the obstacles
a=[
[1,1,1,1,1,1,1],
[1,0,1,1,1,1,1],
[1,1,1,1,1,0,1],
[1,1,0,1,0,1,1],
[1,0,1,0,0,1,1],
[1,1,0,1,1,1,1],
[1,1,0,1,1,1,1]
]

#function to generate environment matrix(b)
#b is a 49x4 matrix with 
#first column denoting up move
#second column denoting down move
#third column denoting right move
#fourth column denoting left move
#-10 value represents an obstacle
#-1 represents a valid move
#100 reward is given for reaching destination
def convert(a):
	b=np.zeros((49,4))
	for i in range(7):
		b[i][0]=-10
	for i in range(7):
		b[(7*i)][3]=-10
	for i in range(7):
		b[(7*i+6)][2]=-10
	for i in range(7):
		b[42+i][1]=-10
	for i in range(7):
		for j in range(7):
			if a[i][j]==0:
				for k in range(4):
					b[7*i+j][k]=-10
	for j in range(7):
		if a[0][j]==0:
			b[j-1][2]=-10
			if j!=6:
				b[j+1][3]=-10
			b[j+7][0]=-10

	for j in range(7):
		if a[6][j]==0:
			if j!=0:
				b[42+j-1][2]=-10
			b[42+j+1][3]=-10
			b[42+j-7][1]=-10

	for i in range(7):
		if a[i][0]==0:
			if i!=6:
				b[7*(i+1)][0]=-10
			b[7*(i-1)][1]=-10
			b[7*i+1][3]=-10
	

	for i in range(7):
		if a[i][6]==0:
			b[7*i+6+7][0]=-10
			if i !=0:
				b[7*i+6-7][1]=-10
			b[7*i+6-1][2]=-10

	for i in range(1,6):
		for j in range(1,6):
			if a[i][j]==0:
				b[7*i+j+1][3]=-10
				b[7*i+j-1][2]=-10
				b[7*i+j+7][0]=-10
				b[7*i+j-7][1]=-10		
	if a[5][6]==1:
		b[41][1]=100
	if a[6][5]==1:
		b[47][2]=100

	for i in range(49):
		for j in range(4):
			if b[i][j]== 0:
				b[i][j]= -1

	return b	

#environment matrix
e_m=convert(a)

#agent matrix
a_m=np.zeros((49,4))

#start position and current position
start=0
current=0

#to find possible moves from a position
def p_moves(current):
	possible_moves=[]
	for i in range(4):
		if e_m[current][i]!=-10 :
			possible_moves.append(i)
		else:
			pass
	return possible_moves

#to find max q value from next location		
def max_q_plus_one(current):
	possible=p_moves(current)
	temp=[a_m[current][i] for i in possible]
	return temp[np.argmax(temp)]

#function for an epoch from start to end point
def epoch(l_rate,gamma):
	current=start
	while current is not 48:
		possible_moves=p_moves(current)
		cm=(current,possible_moves[random.randint(0,len(possible_moves)-1)])#chosen move
		if cm[1] == 0:
			current=current-7
		elif cm[1] == 1:
			current =current+7
		elif cm[1] == 2:
			current=current+1
		elif cm[1] == 3:
			current=current-1
		#updating q value by q learning method
		a_m[cm[0]][cm[1]]=((1-l_rate)*a_m[cm[0]][cm[1]])+(l_rate)*(e_m[cm[0]][cm[1]]+(gamma)*max_q_plus_one(current))

#the main function		
def main(l_rate,gamma,epochs):
	for i in range(epochs):
		epoch(l_rate,gamma)
		if i%1000==0:
			print i
	print a_m

	curr=start
	while curr!=48:
		if(np.argmax(a_m[curr]))==0:
			print "UP"
			curr -=7
		elif(np.argmax(a_m[curr]))==1:
			print "DOWN"
			curr+=7
		if(np.argmax(a_m[curr]))==2:
			print "RIGHT"
			curr +=1
		if(np.argmax(a_m[curr]))==3:
			print "LEFT"
			curr-=1

main(0.05,0.9,10000)