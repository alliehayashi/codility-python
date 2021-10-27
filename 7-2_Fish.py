# given ary A[] and B[]; A[] = fish size (distinct), B[] = direcrtions (0,1)
# https://app.codility.com/demo/results/training8VS725-QR4/

def solution(A, B):
    down = [] #只存downstream
    up = 0
    for i in range(len(A)):
        if B[i] == 1: #downstream
            down.append(A[i])       
            
        else: 
            while (len(down)>0 and A[i]>down[-1]): #upstream>downstreqam的話就持續pop掉
                down.pop()
                
            if len(down) == 0: #一開始B[i]==0 或 check已經被扣光的情況
                up+=1

    return len(down) + up