

list1 = [-2,0,4,3,-4,8,9]

for i in range(len(list1)):
    for j in range(len(list1)):
        if list1[i] < list1[j]:
            sw = list1[i]
            list1[i] = list1[j]
            list1[j] = sw
print(list1)


array = [0, 1, 2, 1, 0, 2, 1, 0]

for i in range(len(array)):
    for j in range(i + 1, len(array)):  # Fix to avoid redundant swaps
        if array[i] > array[j]:  # Correct the comparison
            # Swap elements
            array[i], array[j] = array[j], array[i]

print(array)
