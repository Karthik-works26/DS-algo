from collections import defaultdict 
n = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input()))  
print(arr) 
hashmap = defaultdict(int) 
for i in range(len(arr)):
    hashmap[arr[i]] += 1 
print(hashmap) 
val = [] 
for i in hashmap.values():
    val.append(i) 
print(val) 
steps = 0 
for i in range(len(val)):
    steps = steps + val[i] 
print(steps)
