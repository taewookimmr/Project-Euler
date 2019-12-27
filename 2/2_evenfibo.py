def solution():
    lim = 4*10**6
    answer = 0
    
    head = 1
    present = 2
    while present < lim:
        if present % 2 == 0:
            answer += present
        head, present = present, present+head
    
    print(answer)
    

solution()
        
    