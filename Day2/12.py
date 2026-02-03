from collections import defaultdict 
n = int(input()) 
arr = [] 
for i in range(len(arr)):
    arr.append(int(input())) 
print(arr) 
################################# problems covered in this interview level sessions  
########## problem 1 max distance between two elements in an arrays 
from collections import defaultdict 
def maxdistance(arr):
    hashmap = defaultdict(int)  
    answer = 0
    for i in range(len(arr)):
        if arr[i] in hashmap:
            current = i - hashmap[arr[i]] 
            if current > answer: 
                answer = current 
    return answer 
############# problems 2 counting the pairs with sum k 
def countpairs(arr,k):
    hashmap = defaultdict(int) 
    count = 0
    for i in range(len(arr)):
        complement = k - arr[i]  
        if complement in hashmap: 
            count = count + hashmap[complement] 
        hashmap[arr[i]] += 1 
    return count 
########### problems 3 returning the unique elements in the arrays 
def compute_unique(string1):
    hashmap = defaultdict(int) 
    for char in string1:
        hashmap[char] += 1 
    for i in range(len(string1)): 
        if hashmap[string1[i]] == 1:
            return i 
    return -1 
################ problem 4 to compute the common characters in an arrays of words 
def common_characters(arr):
    minfreq = defaultdict(int) 
    for i in range(ord("a"),ord("z") + 1):
        minfreq[i] = 1000 
    for words in arr:
        counter = defaultdict(int) 
        for char in words: 
            counter[ord(char)] += 1 
        minfreq = min(minfreq[i],counter[i]) 
    answer = [] 
    for i in range(ord("a"),ord("z") + 1):
        while(minfreq[i] > 0):
            answer.append(chr(i)) 
            minfreq[i] -= 1 
    return answer
