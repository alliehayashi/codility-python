# ary A[]; int N:len(A);
# triple(P, Q, R) 0<=P<Q<R<N, A[P] + A[Q] > A[R], A[Q] + A[R] > A[P], A[R] + A[P] > A[Q]

def solution(A):
    A = sorted(A)
    for i in range(0, len(A)-2):
        if(A[i] + A[i+1] > A[i+2]):
            return 1
    return 0    