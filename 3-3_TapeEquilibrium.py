#returns the min of result

def solution(A):
    passed, N, sum = check(A)
    A_list=[]
    now = 0
    if N == 1:
        return 0
    if passed == True:
        for i in range (N-1):
            now += A[i]
            A_list.insert(0, (abs(now-(sum-now))))
    return min(A_list)
    
def check(A):
    #N is an integer within the range [2..100,000];
    N = len(A)  
    if N<2 or N>100000:
        return False, N, 0
    
    #each element of array A is an integer within the range [-1,000..1,000].
    sum = 0
    for i in A:
        if i<-1000 or i>1000:
            return False, N, 0
            break
        else:
            sum+=i
    return True, N, sum