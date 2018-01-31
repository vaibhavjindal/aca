names=["dd", "dd(1)", "dd(2)", "dd", "dd(1)",  "dd(1)(2)", "dd(1)(1)",  "dd",  "dd(1)"]

def FileNaming(names):
	output=[]
	for i in range(len(names)):
		if names[i] not in output:
			output.append(names[i])
		else:
			for j in range(1,15):
				temp=names[i]+"("+str(j)+")"
				if temp not in output:
					output.append(temp)
					break
	return output

print FileNaming(names)