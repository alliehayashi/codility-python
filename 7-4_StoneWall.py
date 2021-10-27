def solution(H):
    check = []
    count = 0
    
    for i in H:
        #print('-'*22)
        #print('i=', end = '')
        #print(i)
        #print('check=', end = '')
        #print(check)
        
        while check and i<check[-1]:
            check.pop()
            count+=1
            #print('pop')
        if check and i == check[-1]:          
            #print('same')
            continue
        check.append(i)
        #print(check)
        #print('append')
    return count + len(check)
            