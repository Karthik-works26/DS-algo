n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

# Edge case
if n < 2:
    print(0)
    exit()

# Maximum subarray sum ending at each index (Kadane)
left = [0] * n
left[0] = arr[0]
for i in range(1, n):
    left[i] = max(arr[i], left[i - 1] + arr[i])

# Convert to prefix maximums
for i in range(1, n):
    left[i] = max(left[i], left[i - 1])

# Maximum subarray sum starting at each index (reverse Kadane)
right = [0] * n
right[-1] = arr[-1]
for i in range(n - 2, -1, -1):
    right[i] = max(arr[i], right[i + 1] + arr[i])

# Convert to suffix maximums
for i in range(n - 2, -1, -1):
    right[i] = max(right[i], right[i + 1])

# Compute answer
answer = 0
for i in range(n - 1):
    answer = max(answer, left[i] + right[i + 1])

print(answer)
