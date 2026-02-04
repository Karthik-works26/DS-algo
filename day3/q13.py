from collections import defaultdict 
n = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
########################### longest consequtive sequence problems 
def longest_consequtive_sequences(arr): 
    present = defaultdict(int) 
    checked = defaultdict(int) 
    maxchain = 0   
    for nums in arr:
        present[nums] = True  
    ############## filled up the present 
    for i in range(len(arr)):
        if arr[i] not in checked and (arr[i] - 1) not in present:
            start = arr[i] 
            currentchain = 0  
            while(present[start]): 
                currentchain += 1 
                checked[start] = True 
                start = start + 1 
            maxchain = max(maxchain,currentchain) 
    return maxchain 
############# single hashmap solutions for LCS problems 
def longest_consecutive_sequence(arr):
    if not arr:
        return 0

    present = set(arr)
    maxchain = 0

    for num in arr:
        # start only if it's the beginning of a sequence
        if num - 1 not in present:
            current = num
            currentchain = 1

            while current + 1 in present:
                current += 1
                currentchain += 1

            maxchain = max(maxchain, currentchain)

    return maxchain

################## longest subarrays with zero sum 
def longest_subarrays_zerosums(arr):
    hashmap = defaultdict(int) 
    maxlen = 0  
    psum = 0 
    for i in range(len(arr)):
        psum += arr[i] 
        if psum == 0:
            maxlen = i + 1 
        if psum in hashmap:
            currentlen = i - hashmap[psum] 
            if currentlen > maxlen:
                maxlen = currentlen 
        hashmap[psum] = i  
    return maxlen
            


