n = int(input()) 
k = int(input()) 
arr = [] 
for i in range(n):
  arr.append(int(input()) 
print(arr) 
def brute_force(arr,k):
  count = 0 
  for i in range(len(arr)): 
    for j in range(i + 1,len(arr)): 
      if abs(arr[i] - arr[j]) == k:
        count = count + 1 
  return count 
from collections import defaultdict 
def optimal_solutions(arr,k):
  count = 0 
  map = defaultdict(int) 
  for i in range(len(arr)): 
    if arr[i] + k in map:
      count = count + map[arr[i] + k] 
    if arr[i] - k in map:
      count = count + map[arr[i] - k] 
    map[arr[i]] += 1 
    return count 
    
    
