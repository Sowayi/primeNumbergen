#n = raw_input ("enter the upper limit")
def primeNumbers (n):
    list_Primes=[]
    #if n is not an integer
    if not isinstance(n, int):
        raise TypeError
    elif n==0 or n==1:
        return []
    #if n is a negative number
    elif n<0:
        return {"Type Error":"No primes for negatives"}
    elif n==2:
        return [1,2]
    else:
        list_Primes.append(1)
        list_Primes.append(2)
        #m=input given within range of 0-n
        #s=incremented value of divisors of m
        #r=value of remainder after modulus operation
        for m in range (0,n+1):
            s = m - 1
            for counter in range (2,m):
                r = m%counter
                if (r == 0):
                    break;
                elif (r != 0 and counter != s):
                    continue
                elif (counter == s and r > 0):
                    list_Primes.append(m)
    return list_Primes
print(primeNumbers (1000))
