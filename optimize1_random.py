import numpy as np
import math
import random
# edit to the name of the input file
f = open('uniqueproducts1.txt', 'r')
n,m = map(int, f.readline().strip().split())
subsets = []
def get_combos(primes,max):
    maxes = [int(math.log(max,i)) for i in primes]
    nums = []
    for i in range(len(primes)):
        pows = [primes[i]**j for j in range(maxes[i]+1)]
        nums+=pows
    # print(nums)
    new_nums = []
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            prod = nums[i]*nums[j]
            if prod <= max:
                new_nums.append(prod)
    return set(new_nums)
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]
# replace from here to line 10 with your own logic
# variables available are just n and m, which are as described in the problem
subsets=[[i for i in range(1,101)],[j for j in range(301,401)]]
assert len({len(i) for i in subsets}) == 1, "Subsets are not of equal size"
primes = primesfrom2to(m).tolist()
num_primes = len(primes)
best_m = 0
for i in range(1000000):
    l1 = random.sample(primes, random.randint(10,num_primes//n))
    l2 = [p for p in primes if p not in l1]
    if n == 3:
        l2_new = random.sample(l2,random.randint(10,num_primes//n))
        l3 = [p for p in l2 if p not in l2_new]
        l2 = l2_new.copy()
    c1 = list(get_combos(l1,m))
    c2 = list(get_combos(l2,m))
    # c3 = list(get_combos(l3,m))
    ma = min(len(c1),len(c2))
    if ma > best_m:
        subsets = [c1[:ma],c2[:ma]]
        best_m = ma
        print(ma)
print(len(subsets[0]),len(subsets[1]))
# change to whatever you want your output file to be called
out = open('output1.txt', 'w')
for s in subsets:
    for i in range(len(s)):
        out.write(str(s[i])+" ")
    out.write("\n")
out.close()
