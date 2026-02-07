n = int(input()) 
arr = [0]*n 
for i in range(len(arr)): 
    l = int(input()) 
    r = int(input()) 
    arr[l] = arr[l] + 1 
    if r + 1 <= n:
        arr[r + 1] = arr[r + 1] - 1 
    print(arr) 
for i in range(1,len(arr)):
    arr[i] = arr[i - 1] + arr[i] 
print(f"final-array status{arr}")
    
    
