# array A[], non-empty; int N = len(A)
# A permutation is a sequence containing each element from 1 to N once, and only once.
# aka permutation 裡不會有重複的數字 且 會在 1-N 內

def solution(A):
    N = len(A) #長度

    #total sum is correct, but it is not a permutation,
    if len(set(A))!= N: #如果有重複值會被去掉，len會少於總數
        return 0

    if N>0 and N<=1000000: #N is an integer within the range [1..100,000];
        total = int((1+N)*N/2) #應該要有的總數
        sum = 0
        for i in A:
            if i>0 and i<=1000000000: #each element of array A is an integer within the range [1..1,000,000,000].
                sum += i

        if sum == total:
            return 1
        else:
            return 0
        