def solution():
    import math
    def isPrime(x): 
        if x%2 :
            candi = [e for e in range(3, int(math.sqrt(x))+1) if e%2]
            while len(candi):
                e = candi.pop(0)
                if x%e==0:
                    return False
            return True 
        else:
            return False
            
    n = 600851475143
    
    s = int(math.sqrt(n))
    for e in range(s, 1, -1):
        if n%e == 0 and isPrime(e):
            print(e)
            return
    
solution()