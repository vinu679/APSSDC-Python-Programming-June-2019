def isprime(n):
    c=1
    if n==2:
        return True
    for i in range(3,n//2+1):
        if n%i==0:
            c=0
            return False
    if c==1:
        return True
 