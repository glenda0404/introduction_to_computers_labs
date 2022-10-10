list1 = ['國文','英文','數學','自然','社會']
list2 = ['50','60','70','80','90']
list3 = ['57','86','73','82','43']
list4 = ['97','96','86','97','83']
dict0={'index':list1,
       'StuA':list2,
       'StuB':list3,
       'StuC':list4}
print (dict0)
A = (int(list2[0])+int(list2[1])+int(list2[2])+int(list2[3])+int(list2[4]))/5 #A's average
B = (int(list3[0])+int(list3[1])+int(list3[2])+int(list3[3])+int(list3[4]))/5 #B's average
C = (int(list4[0])+int(list4[1])+int(list4[2])+int(list4[3])+int(list4[4]))/5 #C's average
print("A學生平均成績："+str(A))#print A's average
print("B學生平均成績："+str(B))#print B's average
print("C學生平均成績："+str(C))#print C's average
chi = (int(list2[0])+int(list3[0])+int(list4[0]))/3#chinese's average
eng = (int(list2[1])+int(list3[1])+int(list4[1]))/3#english's average
math = (int(list2[2])+int(list3[2])+int(list4[2]))/3#math's average
sci = (int(list2[3])+int(list3[3])+int(list4[3]))/3#science's average
soc = (int(list2[4])+int(list3[4])+int(list4[4]))/3#social's average
print("國文平均成績："+str(chi))#print chinese's average
print("英文平均成績："+str(eng))#print english's average
print("數學平均成績："+str(math))#print math's average
print("自然平均成績："+str(sci))#print science's average
print("社會平均成績："+str(soc))#print social's average
