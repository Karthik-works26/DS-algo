################# returning the longest subarray with sum k 
n = int(input()) 
k = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
############# brute force solutions 
def brute_force(arr,k):
    maxlength = 0 
    minlength = float("-inf") 
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            currsum += arr[j] 
            if currsum == k and (j - i + 1) > maxlength:
                maxlength = j - i + 1 
            elif currsum == k and (j - i + 1) < minlength:
                minlength = j - i + 1 
        return maxlength,minlength 
################################################ optimal soln################################################################# 
from collections import defaultdict 
def optimal(arr,k):
    hashmap = defaultdict(int)  
    maxlength = 0                                                                  
    for i in range(len(arr)):
        psum += arr[i] 
        if psum - k in hashmap: 
            currentlength = i - hashmap[psum - k] + 1 
            if currentlength > maxlength:
                maxlength = currentlength 
    return maxlength 
