def sort(num):
    
    x = len(num)

    for i in range(x-1):

        cnt = 0  
        for j in range(0, x-1-i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
		#交換回数
                cnt = cnt + 1 
                
        # 交換が無いなら終了
        if cnt == 0:
            return num

    
    return num

#例
num = [1,10,8,6,5,6,98]
sort(num)
print(num)