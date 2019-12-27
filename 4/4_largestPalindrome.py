def solution():
    def isPalindrome(x):
        tempstr = [e for e in str(x)]
        revstr = reversed(tempstr)
        check = sum([0 if i==j else 1 for i,j in zip(tempstr, revstr)])
        if check:
            return False 
        else :
            return True

    answer=[]
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            if isPalindrome(i*j):
                answer.append([i*j, i, j])
                
    answer.sort()
    print(answer[-1])
solution()        
            