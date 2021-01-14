def isPrime(N):
    # code here
    if N<=1:
        return False
    if N==2 or N==3:
        return True
    if N%2==0 or N%3==0:
        return False
    i=5
    while(i*i<=N):
        if N%i==0 or N%(i+2)==0:
            return False
        i+=6
    return True
