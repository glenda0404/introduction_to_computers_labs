#建立三個串列儲存三位學生的成績和各類成績平均
gradea=[]
gradeb=[]
gradec=[]

averagea=0
averageb=0
averagec=0

chinese=0
english=0
math=0
social=0
science=0

print("開始輸入A學生的成績，請依照 國文、英文、數學、社會、自然 的順序輸入")
#用for存入成績
for i in range(5):
	temp1=input()
	gradea.append(temp1)
	#用while迴圈防呆
	while int(temp1)<=0 or int(temp1)>100:
		print("請輸入1~100的數值!")
		gradea.pop()
		temp1=input()
		gradea.append(temp1)
		if int(temp1)<=100 and int(temp1)>0:
			break

#印出a學生成績
print("A學生成績:")
print("國文:"+gradea[0],"、英文",gradea[1],"、數學",gradea[2],"、社會:",gradea[3],"、自然",gradea[4])
#a學生結束後換行
print()

print("開始輸入B學生的成績，請依照 國文、英文、數學、社會、自然 的順序輸入")
#用for存入成績
for i in range(5):
	temp2=input()
	gradeb.append(temp2)
	#用while迴圈防呆
	while int(temp2)<=0 or int(temp2)>100:
		print("請輸入1~100的數值!")
		gradeb.pop()
		temp2=input()
		gradeb.append(temp2)
		if int(temp2)<=100 and int(temp2)>0:
			break
#印出b學生成績
print("B學生成績:")
print("國文:"+gradeb[0],"、英文",gradeb[1],"、數學",gradeb[2],"、社會:",gradeb[3],"、自然",gradeb[4])
#b學生結束後換行
print()

print("開始輸入C學生的成績，請依照 國文、英文、數學、社會、自然 的順序輸入")
#用for存入成績
for i in range(5):
	temp3=input()
	gradec.append(temp3)
	#用while迴圈防呆
	while int(temp3)<=0 or int(temp3)>100:
		print("請輸入1~100的數值!")
		gradec.pop()
		temp3=input()
		gradec.append(temp3)
		if int(temp3)<=100 and int(temp3)>0:
			break
#印出c學生成績
print("B學生成績:")
print("國文:"+gradec[0],"、英文",gradec[1],"、數學",gradec[2],"、社會:",gradec[3],"、自然",gradec[4])
#c學生結束後換行
print()

#算出每位學生的成績平均
for i in range(5):
	averagea+=int(gradea[i])/5
	averageb+=int(gradeb[i])/5
	averagec+=int(gradec[i])/5
#把各科平均算出來
chinese+=int(gradea[0])/3+int(gradeb[0])/3+int(gradec[0])/3
english+=int(gradea[1])/3+int(gradeb[1])/3+int(gradec[1])/3
math+=int(gradea[2])/3+int(gradeb[2])/3+int(gradec[2])/3
social+=int(gradea[3])/3+int(gradeb[3])/3+int(gradec[3])/3
science+=int(gradea[4])/3+int(gradeb[4])/3+int(gradec[4])/3
#印出平均
print("A學生平均成績:",averagea)
print("B學生平均成績:",averageb)
print("C學生平均成績:",averagec)
print()
print("國文平均成績:",chinese)
print("英文平均成績:",english)
print("數學平均成績:",math)
print("社會平均成績:",social)
print("自然平均成績:",science)