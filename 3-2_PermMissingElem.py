def solution(A):
    #print(check(A))
    is_ok, N, A, sum = check(A)
    
    if is_ok == True:
        if N == 0:
            return 1
        if A[0] != 1:
            return 1
        if sum == 0:
            return 1
        all = int(((1+(N+1))*(N+1))/2)
        
        if all == sum: #last num losting
            return A[-1]+1

        return (all-sum)
    else:
        return 0

def check(A):
    N = len(A)
    A.sort()
    if N<0 or N>1000000:
        return False, 0, A, 0
    
    #the elements of A are all distinct;
    compare = -1
    sum = 0 
    for i in A: 
        if i == compare:
            return False, 0, A, 0
            break
        else:
            compare = i
            sum+=i
    return True, N, A, sum