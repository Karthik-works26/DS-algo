n = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
k = int(input()) 
############ brute force algorithms 
def bruteforce(arr,k):
    count = 0 
    for i in range(len(arr)):
        current_sum = 0 
        for j in range(i,-1,-1): 
            current_sum += arr[i] 
            if current_sum == k:
                count = count + 1 
    return count 
############## prefix sums based approaches 
def optimal_solutions(arr,k):
    pref = [0]*len(arr) 
    pref[0] = arr[0]  
    count = 0 
    for i in range(1,len(arr)):
        pref[i] = pref[i - 1] + arr[i] 
    for i in range(len(arr)):
        for j in range(i,-1,-1):
            if pref[j] == pref[i] + k: 
                count = count + 1 
    return count 
############## hashmap based final operations  
from collections import defaultdict 
def opti2(arr,k):
    hashmap = defaultdict(int) 
    hashmap[0] = 1  
    count = 0
    for i in range(len(arr)):
        psum += arr[i] 
        if psum - k in hashmap:
            count = count + hashmap[psum - k] 
        hashmap[psum] += 1 
    return count 

