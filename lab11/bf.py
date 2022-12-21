import json

#網路上貼的排組-https://www.796t.com/content/1544740385.html?fbclid=IwAR14WgTXrBftrRMDXcBzopmE2EQSQmY6eIvUD4UZamC0oxfMX_rm8QBKsdI

def Perm(arrs): 
    # 若輸入 [1,2,3]，則先取出1，將剩餘的 [2,3]全排列得到 [[2,3],[3,2]]，再將1加到全排列 [[2,3],[3,2]]上變成 [[1,2,3],[1,3,2]]
    # 同理，取出2或者3時，得到的分別是 [[2,1,3],[2,3,1]]和 [[3,1,2],[3,2,1]]
    if len(arrs)==1:
        return [arrs]
    result = []  # 最終的結果（即全排列的各種情況）
    for i in range(len(arrs)):  
        rest_arrs = arrs[:i]+arrs[i+1:]  # 取出arrs中的第 i個元素後剩餘的元素
        rest_lists = Perm(rest_arrs)   # 剩餘的元素完成全排列
        lists = []
        for term in rest_lists:
            lists.append(arrs[i:i+1]+term)  # 將取出的第i個元素加到剩餘全排列的前面
        result += lists
    return result


def BF(input): #先寫看看函式
    N = len(input) #n表示每個input為幾乘幾的矩陣
    templist =[[i] for i in range(N)]
    #把人的排法存到tempassignment
    tempassignment=Perm(templist)
    #設法派給每個人不同的工作，看看組合
    tempcost= 0 #用來暫存cost
    assignment=[]
    cost=0
    for j in range(len(tempassignment)): #要執行排列組合總數那麼多次
        for i in range(N): #然後從每一次的第[0]跑到第[N-1]
            tempcost+=int(input[i][int(tempassignment[j][i][0])]) #計算每一個的cost
        if cost==0: #如果cost等於初始值的話
            cost=tempcost #把tempcost的東西存進去cost
            assignment=tempassignment[j] #然後把tempassignment的第j個塞進assignment

        elif tempcost<cost: #如果新的tempcost比暫存值來得小的話
            cost=tempcost
            assignment=tempassignment[j]
        tempcost=0
    return assignment, cost


with open('input.json', 'r') as inputFile:
    data = json.load(inputFile) # load data
    for key in data:
        input = data[key] # load each input
        # Brute Force Algorithm
        assignment, cost = BF(input)

        print('Question: ' + str(key))
        print('Assignment:', assignment)
        print('Cost:', cost)
        print()