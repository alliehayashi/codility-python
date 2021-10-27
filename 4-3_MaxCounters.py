# array A[], non-empty; int N counters, default:0, int M = len(A)
# rule#1: 如果 1<= A[K] <= N, A[K]的index值+1
# rule#2: 如果A[K]+1 == N, K就是max counter, 整個counters的值都要設跟k一樣的值

def solution(N, A):
    M = len(A)
    if M>0 and M<=1000000 and N>0 and N<=1000000: #N and M are integers within the range [1..100,000];
        counters = [0]*N
        #print(counters)
        for i in A:
            #print('i=', end = '')
            #print(i)
            if i>0 and i<=N:
                counters[i-1] = counters[i-1]+1
                #print(counters)
            if i == N+1:
                #print(max(counters))
                counters = [max(counters)]*N
                #print(counters)
        #print(counters)
        return counters
