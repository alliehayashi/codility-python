# int A; int B, int K 
# [A...B] which could be divided by K
import math
def solution(A, B, K):
    count = 0

    if A>=0 and B>=0 and K>0 and A<=2000000000 and B<=2000000000 and K<=2000000000:
    #A and B are integers within the range [0..2,000,000,000];
    #K is an integer within the range [1..2,000,000,000];   
        if A<=B:
            count = math.floor(B/K) - math.floor(A/K)
            if A%K == 0:
                count+=1
    return count