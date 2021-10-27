import math
def solution(X, Y, D):
    #frog postition X, destination Y, fixed distance D
    #X, Y and D are integers within the range [1..1,000,000,000]
    #X ≤ Y
    if check(X, Y, D) == True:
        
        if X==Y:
            ans = 0
        else:
            if (Y-X)%D == 0:
                ans = int(math.floor(Y-X)/D)
            else:
                ans =  math.floor((Y-X)/D) + 1
        #print(ans)
        return ans    
    else:
        return Exception

def check(X, Y, D):
    if X<0 or Y<0 or D<0:
        return False
    if X>1000000000 or Y>1000000000 or D>1000000000:
        return False
    if Y<X:
        return False
    else:
        return True