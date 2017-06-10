#n = raw_input ("enter the upper limit")
import time
def primeNumbers (n):
    list_Primes=[]
    if not isinstance(n, int):
        raise TypeError
    elif n==0:
        return []
    elif n<0:
        return {"Type Error":"No primes for negatives"}
    elif n==1:
        return [1]
    elif n==2:
        return [1,2]
    else:
        list_Primes.append(1)
        list_Primes.append(2)
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
startTime=time.time()
print(primeNumbers (1000))
print(time.time()-startTime)
