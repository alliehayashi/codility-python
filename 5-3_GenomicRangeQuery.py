# Str S consits nucleotides [A, C, G, T], impact factor[1, 2, 3, 4]
# Query M; arr P[], Q[]: non-empty; 0<=K<=M

def solution(S, P, Q):
    N = len(S) 
    M = len(P)
    dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    string_check = check(S)
    ans = []

    if N>=1 and N<=100000 and string_check == True:        
        #N is an integer within the range [1..100,000];
        if M == len(Q) and M>0 and M<=50000:
            #M is an integer within the range [1..50,000];
            S = list(S)
            
            for i in range (M):
                first = P[i]
                last = Q[i]+1
                ranges = S[first:last]
                ranges.sort()
                ans.append(dict[(ranges[0])])
    return ans
                
def check(S):
    S_check = list(S) #convert string to array
    S_check = set(S_check)
    for i in S_check:
        if i == 'A' or i == 'T' or i == 'C' or i == 'G':
            string_check = True
        else:
            string_check = False  
    
    return string_check