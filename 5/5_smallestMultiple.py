def solution() : 
    def gcd(u, v):
        if v : return gcd(v, u%v)
        else: return u

    n = int(input())
    stack = [e for e in range(1,n+1)]
    answer = stack.pop()
  
    for e in stack[::-1]:
        if answer % e:
            answer *= e//gcd(answer, e)
    
    print(answer )
            

solution()

        