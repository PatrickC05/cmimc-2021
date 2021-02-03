import math
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

p1 = []
total = get_combos(p1,200)
print(len(total))
print(total)
