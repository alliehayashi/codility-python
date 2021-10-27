# ary[A]:non-neg; discs<index>:0~N-1; int N:len(A)
# 解題：A[J] = K; 可知圈之範圍為[J-K, J+K]
# 比較下組之數字，如果其中一個數字位於比較值的範圍內(J-K)~(J+K)，就是有intersect

def solution(A):
    N = len(A)
    count = 0

    if N>0 or N<=1000000:     
        

        for i in range (N-1): #i = 0, 1, 2, 3, 4
            k = i+1
            
            while k < N: 
                J = i-A[i]
                K = i+A[i]
                J_1 = (k)-A[(k)]
                K_1 = (k)+A[(k)]
            
                if ((J <= J_1 and J_1 <= K) or (J <= K_1 and K_1 <= K)) or ((J_1 <= J and J <= K_1) or (K_1 <= K and K <= K_1)):
                    count+=1                    
                k+=1

                if count>10000000:
                    return -1             
    if N == 0:
        return 0        
    
    return count