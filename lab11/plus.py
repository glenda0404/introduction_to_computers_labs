import json

def split(nums, m):
        #value must be in this range
        # 使用夾擊 分為 head => 最大值 tail => 總數  mid => (head + tail) // 2
        head, tail = max(nums), sum(nums)
        def checksplit(target, m):
            cnt = sums = 0
            for num in nums:
                if num + sums > target:
                    cnt += 1
                    sums = 0
                sums += num
            return cnt >= m
        while head <= tail:
            mid = (head + tail)//2 
            if checksplit(mid, m):
                head = mid + 1      # 當切數>m 要變大mid 所以head = mid + 1
            else:
                tail = mid - 1      # 當切數<m 要變小mid 所以tail = mid - 1
        return head                 # 當頭尾發生碰撞 表示為答案 if tail == head return head
    
with open('input_plus.json', 'r') as inputFile:
    data = json.load(inputFile) # load data
    for key in data:
        input = data[key] # load each input
        answer = split(data[key][0],data[key][1])
        print('Question: ' + str(key))
        print('Answer: ' , answer)
        print()
