#coding=utf-8
#複製就對了-開頭，引入flask和request工具
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#建立一個總字典用來存東西
keyval={}

# 【第一個api-若有get request傳送到 / ，回傳"ok"】
@app.route('/',methods=['GET']) #會執行下面第一個函式
def api1():
    return 'ok' #response body 為ok
#測試用，照理來說不會執行出來
def test1():
    return 'not okayyy' 

#【第二個api-新增一個 key-value pair 並回傳’set success’，若key已存在 則回傳’key exist’】
#複製-設定路由為/set，使用 request.form 來接收body的資料，接著用to_dict()這個function來轉成python的dict格式，就可以使用這個資料了
@app.route('/set',methods=['POST'])
def api2():
    to_list = list((request.form.to_dict()).values()) #把資料存成dict後，將值轉成list的形式存在to_list裡面
    
    #每次的key和value都會佔兩格，故to_list[0]會存到key值、to_list[1]會存到value值
    b=to_list[0] in keyval #確認這次的key有沒有在字典裡
    if b==True: #如果此次傳入的key已經記錄過的話
        return 'key exist' #回傳存過了
        
    else: #除此之外，把得到的key和value存到總字典
        keyval[to_list[0]] =to_list[1] 
        return 'set success' #並回傳’set success’
        
#【第三個api-回傳所有存在的 key (記得要轉為str格式)】
@app.route('/key_list',methods=['GET']) #設定路由為/key_list
def api3():
      return str(list(keyval.keys())) #keys()取得以「鍵」為元素的組合，再用str的格式印出來
    
#【第四個api-回傳指定的 key 的資訊，若找不到就回傳’key not found’】
@app.route('/get_value/<key>',methods=['GET']) #設定路由為/get_value/<key>，key作為下方函式可用的路由變數
def api4(key):
    b=key in keyval #確認這次的key有沒有在字典裡
    if b==True: #如果此次傳入的key已經記錄過的話
        return keyval[key] #回傳那個key對應的value值
    else:
        return 'key not found' #如果key未紀錄的話，回傳key not found

#【第五個api-更新指定的 key 的資訊並回傳’update success’，若 key 不存在 則回傳’key does not exist’】
@app.route('/update_value',methods=['POST'])
def api5():
    to_list = list((request.form.to_dict()).values()) #把資料存成dict後，將值轉成list的形式存在to_list裡面
    b=to_list[0] in keyval #確認這次的key有沒有在字典裡
    if b==True: #如果此次傳入的key已經記錄過的話
        keyval[to_list[0]] = to_list[1] #把得到的value重新存成總字典裡key對應的值
        return'update success' #成功更新!
        
    else: #除此之外告訴他key不存在
        return 'key does not exist'
        
#【第六個api-刪除指定的 key 的資訊並回傳’delete success’，若找不到就回傳’key not found’】
@app.route('/delete/<key>',methods=['GET'])#設定路由為/delete/<key>，key作為下方函式可用的路由變數
def api6(key):
    b=key in keyval #確認這次的key有沒有在字典裡
    if b==True: #如果此次傳入的key已經記錄過的話
        del keyval[key] #刪除它的值
        return 'delete success'
    else:
        return 'key not found' #除此之外，跟他說沒有此key

# 複製-將webserver執行，監聽任意來源ip，port開在3000，開啟debug模式，每次檔案更新後，webserver會自動重啟，不需要手動重啟
app.run(host="0.0.0.0", port=3000, debug=True)
