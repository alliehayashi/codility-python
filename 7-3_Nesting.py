# string S consists only of the characters "("

def solution(S):
    check = []
    for i in S:
        if i == '(': #加入檢查列
            check.append(i)
        elif len(check)>0 and i == ')' and check[-1] == '(':
            check.pop()
        elif len(check) == 0 and i == ')': #
            return 0
    if len(check) == 0:
        return 1
    return 0