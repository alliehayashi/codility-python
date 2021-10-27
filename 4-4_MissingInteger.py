#ary A; int N
#return value has to be postive number

def solution(A):
    N = len(A)
    if N>0 and N<=100000: #N is an integer within the range [1..100,000];
        A = set(A)
        A = (sorted(A))
        min = 0
        for i in A:
            if i>=-1000000 and i<=1000000:
                if N==1: #只有一個值的情況
                    if i!=1: #是1或是負值
                        return 1
                    else:
                        return 2

                if i>0:
                    if i-min == 1: 
                        min = i

                    if i-min > 1 and min>0 : #相差大於1, return ans
                        return min+1 #
                if i<0:
                    continue
                     
        if min<0: #整個ary都是負數
            return 1
        else:
            return min+1