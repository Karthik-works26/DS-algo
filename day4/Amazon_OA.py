from collections import defaultdict

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

print(arr)

mp = defaultdict(int)
for num in arr:
    mp[num] += 1

print(mp)

count_ops = 0

for freq in mp.values():
    if freq == 1:
        print(-1)
        exit()
    if freq % 3 == 0:
        count_ops += freq // 3
    else:
        count_ops += freq // 3 + 1

print(count_ops)
