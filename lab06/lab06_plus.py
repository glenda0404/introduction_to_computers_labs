#匯入random模組並取名r
import random as r 
#骰子字典
Times = {"One":0, "Two":0, "Three":0, "Four":0, "Five":0, "Six":0}
#把Times的keys存到list1
list1=list(Times.keys())
#重作1000000次
for i in range(1000000):
        #在0~5之間取亂數
        x=r.randint(0, 5) 
        #把keys加0.0001%
        Times[list1[x]] = Times[list1[x]] + 1/10000
#用for迴圈輸出六次
for i in range(0,6):
        print ("The probability of "+list1[i]+" is "+str(round(Times[list1[i]],2))+"%" )
#取Times字典裡第i個key的value到小數點第二位