#青蛙要跳到x距離, given A[], 葉子每秒會落在不同的Ｘ, 鋪滿1-X後青蛙才能過岸
#A[]裡面的數字一定是1-X的範圍, 求i

def solution(X, A):
    if X-0>=1 and len(A)>0:
        A_list=set() #set會去除重複值
        if X == len(A) and len(A) == 1:
            return 0

        for i in range(len(A)):
            A_list.add(A[i]) #新數字加入set
            if len(A_list) == X:
                return i 
        return -1 #無法過則return -1