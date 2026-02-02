######### implementing the counting concepts  
from collections import defaultdict 
import sys 
n = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
def brute_force(arr):
    maxcount,mincount = 0,sys.maxsize() 
    maxele,minele = 0,0 
    for i in range(len(arr)): 
        count = 0 
        for j in range(i,len(arr)):
            if arr[i] == arr[j]:
                count = count + 1 
        if count > maxcount:
            maxcount = count 
            maxele = arr[i] 
        if count < mincount:
            mincount = count 
            minele = arr[i] 
    return maxele,minele 
def optimal_solutions(arr):
    hashmap = defaultdict(int) 
    for nums in arr:
        hashmap[nums] += 1 
    maxcount = max(hashmap.values()) 
    mincount = min(hashmap.values()) 
    maxele = [(k,v) for (k,v) in hashmap.items() if v == maxcount] 
    minele = [(k,v) for (k,v) in hashmap.items()if v == mincount] 
    return maxele,minele 
 
