# ary A[]:non-empty; int N:len(A)
# 0 <= P < Q < R < N

def solution(A):
    N = len(A)
    
    if N>=3 and N<=1000000:
        A = sorted(A)
        #print(A)
        front = A[0]*A[1]*A[2]
        back = A[-1]*A[-2]*A[-3] 
     
        if A[-1]>0 and A[-1]<=1000: #正負數混雜or都是正數
            if A[0]*A[1] > A[-1]*A[-2] or A[0]*A[1] > A[-3]*A[-2]: #如果最負數乘積>第1-2大or第2-3大正數
                ans = A[0]*A[1]*A[-1]
            else: 
                ans = back

        if A[-1]<=0 and A[0]>=-1000: #都是負數 取最小值
            if front < back or A[-1] == 0: #如果最大值為0 且 後三組數字較大
                ans = back
            else : 
                ans = front                 
    return ans