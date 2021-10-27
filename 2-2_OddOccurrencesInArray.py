# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    for i in A: #[check] 
        if i<0 or i>1000000000:
            
    
    N = len(A) #[check] if is *empty*, *too long* or not even
    #print(N)
    if N<0 or N>1000000 or N%2!=1:
        exit
    if N==0:
        return A[0]
    A.sort()
    #print(A)
 
    while (A[0] == A[1]):
        #print(A[0])
        #print(A[1])
        A.pop(0)
        A.pop(0)
        #print(A)

    return A[0]