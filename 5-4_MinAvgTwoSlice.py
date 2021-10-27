# ary A[]:non-empty; int N:len(A); 
# (P, Q), at least contains two elements, 0<=P<Q

def solution(A):
    dict = {}
    N = len(A)
    if N>=2 and N<=1000000:
        for i in range N: