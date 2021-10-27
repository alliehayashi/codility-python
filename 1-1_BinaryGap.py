def solution(N):
    N = "{0:b}".format(N) #str to binary
    max_count = 0 #累計最大數值
    count = 0 #本次計算數值

    for i in N:
        if i == '0':
            count+=1 #計算0的個數（區間）
   
        elif i == '1':
            if count>max_count: #本次>max, 將本次值給max
                max_count = count
            count = 0 #不管是否大於max_count, 都需要歸零重新計算
                
    return max_count

    