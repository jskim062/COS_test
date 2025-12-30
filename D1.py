def solution(size):

    SOL = [0,0,0,0,0,0] #sol 정의
    
    for ch in size:    #size 따른 SOL 정의
        if ch == "XS" :
            SOL[0]+=1
        elif ch == "S" :
            SOL[1]+=1
        elif ch == "M" :
            SOL[2]+=1
        elif ch == "L" :
            SOL[3]+=1
        elif ch == "XL" :
            SOL[4]+=1
        elif ch == "XXL" :
            SOL[5]+=1

    return SOL
                   
size_list = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(size_list)

print("[XS, S, M, L, XL, XXL] = ", ret)

