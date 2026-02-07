######## Flagged subarrays problems 
## Amazon OA on flagged array problem 
n = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
k = int(input()) 
print(k) 
def brute_force(arr,k):
    count = 0 
    for i in range(len(arr)): 
        curr_sum = 0
        for j in range(i,len(arr)): 
            curr_sum += arr[j] 
            if curr_sum%k == j - i + 1:
                count = count + 1 
    return count 
### optimal hashmap based algorithms 
from collections import defaultdict 
def solve(arr,k):
    hashmap = defaultdict(int) 
    pref = [0]*len(arr) 
    pref[0] = arr[0] 
    count = 0 
    for i in range(1,len(arr)):
        pref[i] = pref[i - 1] + arr[i] 
    for j in range(len(arr)): 
        if pref[j] - j in hashmap: 
            count = count + hashmap[pref[j] - j] 
        rhs = pref[j - 1] - j + 1 
        hashmap[rhs] += 1 
    return count  
  n = int(input()) 
arr = [] 
for i in range(n):
  arr.append(int(input()) 
print(arr)  
k = int(input())
print(solve(arr,k)) 
             
    
            
        
