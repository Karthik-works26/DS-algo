############### ideas of prefix sums computations problems 
n = int(input()) 
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
l = int(input()) 
r = int(input()) 
def brute_force(arr,l,r):
    answer = 0 
    for i in range(l,r + 1):
        answer = answer + arr[i] 
    return answer 
################## optimal solution of prefix arrays concept 
def optimal1(arr,l,r): 
    prefix_arrays = [0]*len(arr) 
    prefix_arrays[0] = arr[0] 
    for i in range(1,len(arr)):
        prefix_arrays[i] = prefix_arrays[i - 1] + arr[i]  
    print(prefix_arrays)
    solution = prefix_arrays[r] - prefix_arrays[l - 1] 
    return solution 
print(brute_force(arr,l,r)) 
print(optimal1(arr,l,r)) 
######### important prequisite for hard OA problems 
