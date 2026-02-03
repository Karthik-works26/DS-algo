#################### solving the problems of interview level 
n = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
################################## frequency printer problems 
from collections import defaultdict 
def frequency_printers(arr):
    hashmap = defaultdict(int) 
    for nums in arr:
        hashmap[nums] += 1 
    return hashmap 
###################### counting pairs whose sums is k 
def count_pairs(arr,k):
    count = 0 
    hashmap = defaultdict(int) 
    for i in range(len(arr)):
        complement = k - arr[i] 
        if complement in hashmap:
            count = count + hashmap[complement] 
        hashmap[arr[i]] += 1 
    return count 
################ prefix sums queries SPOJ problem  
def prefix_queries(arr,l,r): 
    prefix = [0]*len(arr) 
    prefix[0] = arr[0] 
    for i in range(1,len(arr)):
        prefix[i] = prefix[i - 1] + arr[i] 
    answer = prefix[r] - prefix[l - 1] 
    return answer 
