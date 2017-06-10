#n = raw_input ("enter the upper limit")
import time
def primeNumbers (n):
    list_Primes=[]
    for m in range (0,n):
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
        
start = time.time()
print(primeNumbers (50000))
print (time.time() -start)
