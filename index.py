
arr = [10, 20, 30, 40, 50]

n = len(arr)

temp = [0] * n

for i in range(n):
    temp[i] = arr[n - i - 1]

print("Original Array:", arr)
print("Reversed Array:", temp)
