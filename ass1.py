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

