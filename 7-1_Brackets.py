# 先將左半邊的字符存起來至chech[], 再來檢查是否右半的字符有跟check[]的字元match到

def solution(S):
    check = []

    if len(S)>0:
        for i in S:
                if i == '(' or i == '[' or i == '{':
                    check.append(i)

                else:
                    if len(check) == 0: #都沒有檢到字符的狀況
                        return 0
                        
                    if i == ')' and check[-1] == '(':
                        check.pop() #default pop [-1]

                    elif i == ']' and check[-1] == '[': #use elif so that it don't evaluate the rest condictions
                        check.pop() 
                   
                    elif i == '}' and check[-1] == '{':
                        check.pop()        
                                 
                    else:
                        return 0
        return 1 if len(check) == 0 else 0
    
    if len(S) == 0:
        return 1