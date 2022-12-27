import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
f = open('Temperature.txt')
bye=f.readline()    #用來刪掉第一行
temp_list=[]

for line in f.readlines():
    s = line.split("\n")
    s_dropna = list(filter(None, s))    #把空值刪掉
    s2 =list(map(float,s_dropna[0].split(","))) #把裡面換成float
    s2 =s2[1:] #不要取到年份
    temp_list.append(s2) #把取好的值存進去總list
f.close

# 【開始畫第一張圖】
month = np.array(range(1,13))
year=[2013,2014,2015,2016,2017,2018,2019,2020,2021]

for i in range(9):
    plt.plot(month, temp_list[i], label=str(year[i]))
a =MultipleLocator(1)
plt.gca().xaxis.set_major_locator(a)
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend(loc = 8)
plt.show()

#【第二張圖的程式碼】

total=[]
temptsum=0
meansum=0 #用來算總平均溫度的
for i in range(12):
    temptsum=0
    for j in range(9): #把九年中的同一個月抓出來加
        temptsum+=temp_list[j][i]   
        meansum+=temp_list[j][i]  
    total.append(round((temptsum/9),2)) #每個月的總和/9，存進一個list裡
print(total)
print(round(meansum/(9*12),2)) 
#【畫第二張圖】

month = np.array(range(1,13))
year=[2013,2014,2015,2016,2017,2018,2019,2020,2021]

plt.plot(month,total,color='b',)
plt.scatter(month,total,color = 'r')
for i in range(len(month)):
    plt.text(month[i],total[i],str(total[i]))
plt.text(1, round(meansum/(9*12),2), round(meansum/(9*12),2) ,va = 'bottom', fontsize = 10)
plt.axhline((round(meansum/(9*12),2)),label='Mean of 9 Years',color='r',linestyle='--') #用總和除以總月份數算平均，然後限制一下小數位數、再加上虛線與顏色等條件
plt.gca().xaxis.set_major_locator(a)
plt.yticks(range(16,34,2))
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend()
plt.show()

fig = plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
for i in range(9):
    plt.plot(month, temp_list[i], label=str(year[i]))
a =MultipleLocator(1)
plt.gca().xaxis.set_major_locator(a)
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend()
plt.subplot(1,2,2)
plt.plot(month,total,color='b',)
plt.scatter(month,total,color = 'r')
for i in range(len(month)):
    plt.text(month[i],total[i],str(total[i]))
plt.axhline((round(meansum/(9*12),2)),label='Mean of 9 Years',color='r',linestyle='--') #用總和除以總月份數算平均，然後限制一下小數位數、再加上虛線與顏色等條件
plt.gca().xaxis.set_major_locator(a)
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend()
fig.savefig('lab13_03.png')