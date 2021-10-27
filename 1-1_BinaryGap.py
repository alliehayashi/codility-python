def solution(N):
    # write your code in Python 3.6
    value = "{0:b}".format(N)
    gap_max_length = 0  #遇到1後，將目前為止最大的gap length存入
    gap_count = 0  #累積計算目前的gap length
    #print(value)
    for i in value:
        if i == '0':
            gap_count+=1
        elif i == '1':
            if gap_count > gap_max_length:
                gap_max_length = gap_count
                gap_count = 0
    
    return gap_max_length
    pass
        
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

    