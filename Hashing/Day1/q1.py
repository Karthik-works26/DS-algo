############### counting frequencies problems 
n = int(input()) 
q = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
def brute_force(arr,q): 
    for i in range(q): 
        query = int(input()) 
        count = 0 
        for j in range(len(arr)):
            if arr[j] == query:
                count = count + 1 
    return count 
############ optimal solutions to solve 
def optimal_1(arr,q):
    hash_arr = [0]*(max(arr)) 
    for i in range(len(arr)):
        c = arr[i] 
        hash_arr[c] = hash_arr[c] + 1  
    for i in range(q):
        query = int(input()) 
        count =  hash_arr[query] 
        print(count) 
############## space optimisations 
from collections import defaultdict 
def optimal_2(arr,q): 
    hashmap = defaultdict(int) 
    for nums in arr:
        hashmap[nums] += 1 
    for i in range(q):
        query = int(input())
        count = hashmap[query] 
        print(count) 
        
