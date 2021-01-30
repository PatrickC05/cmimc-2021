# edit to the name of the input file
f = open('input.in', 'r')
n,m = map(int, f.readline().strip().split())
subsets = []
# replace from here to line 10 with your own logic
# variables available are just n and m, which are as described in the problem
for _ in range(n):
    # populate sets with lists of the sets you want

    subsets.append([1,2])
print(subsets)
assert len({len(i) for i in subsets}) == 1, "Subsets are not of equal size"

# change to whatever you want your output file to be called
out = open('output.txt', 'w')
for s in subsets:
    for i in range(len(s)):
        out.write(str(s[i])+" ")
    out.write("\n")
out.close()
