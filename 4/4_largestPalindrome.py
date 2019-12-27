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


## isPalindrome이 효율을 올렸더라도
## body 부분에서 효율을 올릴 여지는 남아있다.
## 2중 반복문을 모두 순회하면서 list에 append할 필요가 있을까?
## break 조건으로 어떤 조건을 삼으면 될까 고민해보자.
## 현재 이 틀을 바꾸는 것도 생각해봐야겠지, 다른 틀에서 더 효율적으로 문제를 풀어낼 수 있으니.            