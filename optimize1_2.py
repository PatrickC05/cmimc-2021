import math
def get_combos(primes,max):
    maxes = [int(math.log(max,i)) for i in primes]
    print(maxes)
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

p1 = [2,101]
p2 = [3,11]
p1 = [5,7,199]
p1 = [13,17,19,23, 29, 31, 37]
p1 = [41, 43, 47, 53, 59, 61, 67, 71]
p1 = [89, 97, 101, 103, 107, 109, 113, 127]
p1 = [131, 137, 139, 149, 151, 157, 163,167]
p1=[173, 179, 181, 191, 193, 197]
total = get_combos(p2,200)
print(len(total))
print(total)
