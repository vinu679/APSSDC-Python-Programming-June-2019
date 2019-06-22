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
 
#Function to determine number of Prime factors for a given number
def numberOfPrimeFactors(n):
    if isPrime(n):
        return 1
    count = 0
    for i in range(2, n // 2 + 1):
        if isPrime(i) and n % i == 0:
            count += 1
    return count