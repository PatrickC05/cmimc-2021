import numpy as np
import math
# edit to the name of the input file
f = open('uniqueproducts4.txt', 'r')
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
print(len(primes))
def get2k(remain_primes,k, max, cur_in=[]):
    combos = get_combos(cur_in,max)
    if len(combos) > k:
        raise ValueError()
    if len(combos) == k:
        return cur_in,remain_primes
    for p in remain_primes:
        new_remain = remain_primes.copy()
        new_remain.remove(p)
        new_in = cur_in.copy()
        new_in.append(p)
        try:
            return get2k(new_remain,k,max,new_in)
        except ValueError:
            pass
for k in range(300,m//n):
    active_primes = primesfrom2to(m).tolist()
    cur_subsets = []
    print(k)
    try:
        for i in range(n):
            new_subset, active_primes = get2k(active_primes.copy(),k,m)
            cur_subsets.append(list(get_combos(new_subset,m)))
        subsets = cur_subsets.copy()
        for s in subsets:
            for i in range(len(s)):
                print(str(s[i])+" ")
        print("-----------")
    except (ValueError, TypeError):
        break
print(subsets)
assert len({len(i) for i in subsets}) == 1, "Subsets are not of equal size"

# change to whatever you want your output file to be called
out = open('output4.txt', 'w')
for s in subsets:
    for i in range(len(s)):
        out.write(str(s[i])+" ")
    out.write("\n")
out.close()
