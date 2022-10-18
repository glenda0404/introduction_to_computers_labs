#函式
def gcd(a,b):
	x,y=a,b
	#若有0的情況
	if x==0 or y==0:
		print("0沒有gcd")
		return 0
	#把比較大的數統一放在x
	if x<y:
		x,y=y,x
	#用while寫輾轉相除法，直到一邊歸零
	while y!=0:
		r=x%y
		x=y
		y=r
	#最大公因數=1時兩數互質
	if x==1:
		print(str(a)+"和"+str(b)+"互質")
	#印出值
	else:
		print(str(a)+"和"+str(b)+"的gcd="+str(x))
#印出題目要的值
ans1=gcd(80,20)
ans2=gcd(10,0)
ans3=gcd(19,20)

