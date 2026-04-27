arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = sorted(arr)

print("Sorted array using sorted():", *sorted_arr)

arr.sort()
print("Sorted array using list.sort():", *arr)
