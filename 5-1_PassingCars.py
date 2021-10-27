#ary A[], non-empty; int N = len(A); 
# each element of array A is an integer that can have one of the following values: 0, 1.

def solution(A):
    N = len(A)
    base = 0
    count = 0

    if N>0 and N<=100000:  #N is an integer within the range [1..100,000];
        for i in range(N):
            if A[i] == 0 or A[i] == 1:  #each element of array A is an integer that can have one of the following values: 0, 1.          
                if A[i] != 1:
                    base+=1
                else:
                    count+=base                
        if count>1000000000:
            count = -1
        return count           