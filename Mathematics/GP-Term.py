def termOfGP(A,B,N):
    #Your code here
    if N==1:
        return A
    if N==2:
        return B
    r=B/A
    return math.floor(A*math.pow(r,N-1))

