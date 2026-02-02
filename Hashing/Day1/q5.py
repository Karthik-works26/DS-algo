########## pair sum problems 
n = int(input()) 
k = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
def brute_force(arr,x):
    count = 0 
    for i in range(len(arr)):
        for j in range(i + 1,len(arr)):
            if arr[i] + arr[j] == k:
                count = count + 1 
    return count 
from collections import defaultdict 
def optimal_solve(arr,k):
    count = 0 
    hashmap = defaultdict(int) 
    for nums in arr: 
        complement = k - nums 
        if complement in hashmap:
            count = count + hashmap[complement] 
        hashmap[nums] += 1 
    return count 

