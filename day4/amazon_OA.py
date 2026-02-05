from collections import defaultdict  

s = input()
t = input()

m1 = defaultdict(int)
m2 = defaultdict(int)

for char in s:
    m1[char] += 1

for char in t:
    m2[char] += 1  

print(m1)
print(m2)

ans = float("inf")

for char in m2:
    if m1[char] == 0:
        ans = 0
        break
    ans = min(ans, m1[char] // m2[char])

if ans == 0:
    print("no more replications")
else:
    print(ans)
