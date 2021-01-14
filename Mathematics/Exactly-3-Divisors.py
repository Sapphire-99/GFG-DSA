def isprime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0 :
        return False
    k=5
    while(k*k<=n):
        if n%k==0 or n%(k+2)==0:
            return False
        k+=6
    return True
        
def exactly3Divisors(N):
    # code here
    co=0
    i=2
    while(i*i<=N):
        if isprime(i):
            co+=1
        i+=1
    return co
