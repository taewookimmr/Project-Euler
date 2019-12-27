def solution():
    
    def isPalindrome_not_efficient(x):
        tempstr = [e for e in str(x)]
        revstr = reversed(tempstr)
        check = sum([0 if i==j else 1 for i,j in zip(tempstr, revstr)])
        if check:
            return False 
        else :
            return True
        
    def isPalindrome_efficient(x):
        tempstr=[e for e in str(x)]
        n = len(tempstr)
        for i in range(n//2):
            if tempstr[i] != tempstr[-(i+1)]:
                return False
        return True
         
    def body():
        answer=[]
        for i in range(999, 99, -1):
            for j in range(i, 99, -1):
                if isPalindrome_efficient(i*j):
                    answer.append([i*j, i, j])
                    
        answer.sort()
        print(answer[-1])
    
    body()
    
solution()        


##             