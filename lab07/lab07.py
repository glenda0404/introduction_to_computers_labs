 class animal():
	def __init__(self,weig,mood):
		self.weig=weig
		self.mood=mood
	def feed(self,weig,mood):
		pass
	def walk(self,weig,mood):
		pass
	def bath(self,n_bath):
		self.mood=self.mood-2*n_bath
		
#建立animal的子類別dogs
class dogs(animal):
	def __init__(self,weig,mood):
		self.weig=weig
		self.mood=mood
	def feed(self,n_feed):
		self.weig=self.weig+0.2*n_feed
		self.mood=self.mood+n_feed
	def walk(self,n_walk):
		self.weig=self.weig-n_walk*0.2
		self.mood=self.mood+2*n_walk
	def bath(self,n_bath):
		self.mood=self.mood-2*n_bath
	def cout(self,n_feed,n_walk,n_bath):
		self.feed(n_feed)
		self.walk(n_walk)
		self.bath(n_bath)
		print("狗狗現在的體重= ",self.weig,"kg,心情= ",self.mood)
		
#建立animal的子類別cats		
class cats(animal):
	def __init__(self,weig,mood):
		self.weig=weig
		self.mood=mood
	def feed(self,n_feed):
		self.weig=self.weig+0.2*n_feed
		self.mood=self.mood+n_feed
	def walk(self,n_walk):
		self.weif=self.weig-0.2*n_walk
		self.mood=self.mood-n_walk
	def bath(self,n_bath):
		self.mood=self.mood-2*n_bath
	def cout(self,n_feed,n_walk,n_bath):
		self.feed(n_feed)
		self.walk(n_walk)
		self.bath(n_bath)
		print("貓貓現在的體重= ",self.weig,"kg,心情= ",self.mood)
#輸出

#狗
dog = dogs(4.8, 65) 
dog.cout(18,10, 4)
#貓
cat = cats(8.2,60)
cat.cout(40,7,1)
