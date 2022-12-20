import requests
import pymysql

r = requests.get('https://soa.tainan.gov.tw/Api/Service/Get/03b66cb1-a3d1-4c9d-a029-d27cea30c67a')
a = r.json()
#print(data)
data = a["data"]
#資料庫連線設定
db = pymysql.connect(host='localhost', port=3306, user='E94111122', passwd='0219', charset='utf8' , database='wordpress')
#建立操作游標
cursor = db.cursor()

for find in data:
    # sql = """INSERT INTO 110年11月離婚人數按性別及原屬國籍（地區）分(區域別, 性別, 總計總計, 總計本國籍合計) (區域別, 性別, 總計總計, 總計本國籍合計) VALUES ('" + find['區域別'] + "','" + find['性別'] + "', '" + find['總計總計'] + "','"+ find['總計本國籍合計'] +"')"""
    sql = "INSERT INTO `110年11月離婚人數按性別及原屬國籍（地區）分(區域別, 性別, 總計總計, 總計本國籍合計)` (`區域別`, `性別`, `總計總計`, `總計本國籍合計`) VALUES ('" + find['區域別'] + "','" + find['性別'] + "', '" + find['總計總計'] + "','"+ find['總計本國籍合計'] +"')"
    try:
      cursor.execute(sql)
      #提交修改
      db.commit()
    except:
      #發生錯誤時停止執行SQL
      db.rollback()
      print('error')

#關閉連線
db.close()
