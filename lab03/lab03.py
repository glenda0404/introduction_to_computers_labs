#【第一部分】

#num存使用者輸入的數字(字串型態)
num = input("1.please input a number:")
#判斷奇偶數
if int(num) % 2 == 0:
    print("this is even")
else:
    print("this is odd")

#【第二部分】

#分別存入學號的字母與數字
first = input("2.please input your student ID first charcter:")
last = input("3.please input your student ID last 8 numbers:")
#判斷奇偶數
if int(last) % 2 == 0:
    print("your ID number is even")
else:
    print("your ID number is odd")
#輸出學號
print("your student ID is:" + first + last)
