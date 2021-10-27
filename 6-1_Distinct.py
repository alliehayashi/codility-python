# ary A; int N:len(A); -> return distinvt values in A

def solution(A):
    N = len(A)

    if N>0 and N<=100000:
        A = set(A)
        for i in A:
            if i>=-1000000 and i<=1000000:
                ans = len(A) 
    if N == 0:
        ans = 0
    return ans