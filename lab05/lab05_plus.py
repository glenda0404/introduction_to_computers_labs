#建立dic存取
dict0={}
for i in range(4):
	key=input("Enter key: ")
	value_list=[]
	for j in range(5):
		value=input("Enter value: ")
		value_list.append(value)
		dict0[key] = value_list
#完整印出dic
print(dict0)
