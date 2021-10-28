def solution(A, K):
    if len(A) == 0:
        return []
    if(K >= 0 & K <= 100):
    #[check]N and K are integers within the range [0..100]
        for i in A:
            if i >= -1000 & i <= 1000: 
            #[check]each element of array A is an integer within the range [-1,000..1,000].
                continue
            else:
                break
        
    for i in range (K):
        A.insert(0, A[-1]) #insert last one to index[0]
        A.pop(-1) #delete the last one which inserted
    return A