#引入os模組
import os

#以path儲存當前工作目錄，以"/"分隔
path = os.getcwd()
list_path = path.split("/")
#刪除第一個空格(/前)
del list_path[0]
#印出list
print(list_path)

#建立文字檔
txt = 'E94116106.txt'
f = open(txt, 'w')
for i in range(len(list_path)):
  f.write(list_path[i]+os.linesep) #路徑+換行
#抓絕對路徑/home/E94116106
path = os.chdir('/home/E94116106/')

#印出當前目錄下所有檔案和資料夾
file = os.listdir(path)
print(file)
f.write(os.linesep)
for i in range(len(file)):
  f.write(file[i]+os.linesep)
f.close()
