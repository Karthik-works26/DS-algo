############ implementing the problems on the 
n = int(input()) 
k = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input()))
print(arr) 
def brute_force(arr,k):
    for i in range(len(arr)):
        for j in range(i + 1,len(arr)):
            if arr[i] == arr[j] and j - i <= k:
                return True 
    return False 
from collections import defaultdict 
def optimal_solve(arr,k):
    hashmap = defaultdict(int) 
    for nums in arr:
        if nums in hashmap: 
            distance = i - hashmap[nums] 
            if distance <= k:
                return True 
        hashmap[nums] = hashmap[nums] + 1 
    return False 
 
