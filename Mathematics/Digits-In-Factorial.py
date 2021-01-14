def digitsInFactorial(N):
    # code here
    res=1
    for i in range(1,N+1):
        res=res*i
    return math.floor(math.log10(res))+1

