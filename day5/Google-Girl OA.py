n = int(input())  
k = int(input())
arr = [] 
for i in range(n):
    arr.append(int(input())) 
print(arr) 
######## creating the range update tricks 
b = [0]*2000 
for i in range(len(arr)):
    l = arr[i] - k 
    r = arr[i] + k 
    b[l] = b[l] + 1 
    b[r + 1] = b[r + 1] - 1 
for i in range(1,len(b)):
    b[i] = b[i - 1] + b[i] 
print(max(b)) 
