from collections import defaultdict 
n = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
def digit_sum(number):
    curr_sum = 0 
    while number > 0:
        ld = number%10 
        curr_sum = curr_sum + number%10 
        number = number // 10 
    return curr_sum 
def brute_force(arr):
    maxsum = 0 
    for i in range(len(arr)): 
        current_sum = 0 
        for j in range(i + 1,len(arr)): 
            if digit_sum(arr[i]) == digit_sum(arr[j]):
                current_sum = arr[i] + arr[j]  
                maxsum = max(maxsum,current_sum) 
    return maxsum 
def optimal_solution(arr):
    hashmap = defaultdict(int)  
    maxsum = 0
    for i in range(len(arr)):
        dsum = digit_sum(arr[i]) 
        current_sum = 0 
        if dsum in hashmap:
            current_sum = arr[i] + hashmap[dsum] 
            maxsum = max(maxsum,currentsum) 
            hashmap[dsum] = max(hashmap[dsum],arr[i]) 
        else:
            hashmap[dsum] = arr[i] 
    return maxsum 
    
