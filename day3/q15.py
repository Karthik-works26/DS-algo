from collections import defaultdict 
n = int(input()) 
k = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
############## finding the prefix common elements of the arrays 
def prefix_common(a,b):
    hashmap = defaultdict(int)   
    cnt = 0  
    answer = []
    if a[0] == b[0]:
        cnt += 1    
    hashmap[a[0]] += 1 
    hashmap[b[0]] += 1 
    for i in range(len(arr)):  
        if a[i] == b[i]: 
            count = count + 1 
        if a[i] in hashmap:
            count = count + 1 
        if b[i] in hashmap: 
            count = count + 1 
        hashmap[a[i]] += 1 
        hashmap[b[i]] += 1 
        answer.append(count) 
    return answer 
####### leetcode contest level hashing problems 
##### time complexity is O(N) and auxiliary space is O(N) 
