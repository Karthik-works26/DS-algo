############ count of subarrays with given sums and subarrays with given XORs 
n = int(input()) 
k = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
from collections import defaultdict 
def count_of_subarrays_with_sumk(arr,k):
    hashmap = defaultdict(int) 
    count =  0 
    psum = 0  
    hashmap[0] = 1  
    for i in range(len(arr)):  
        psum += arr[i] 
        if psum - k in hashmap:
            count = count + hashmap[psum - k] 
        hashmap[psum] += 1 
    return count 
############## count of subarrays with given xor writing the brute force algorithms 
def count_with_given_xor(arr,k):
    hashmap = defaultdict(int) 
    count = 0 
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]^arr[j] == k:
                count = count + 1 
    return count 
##### the brute force algorithms takes O(N^2) time and O(1) auxiliary space  


