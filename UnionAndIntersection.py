def find_union_and_intersection(arr1, arr2):
    # Using sets for union and intersection
    union = list(set(arr1) | set(arr2))  # Union using set union operator
    intersection = list(set(arr1) & set(arr2))  # Intersection using set intersection operator
    return union, intersection

# Example usage
arr1 = [1, 2, 2, 3, 4]
arr2 = [3, 4, 4, 5, 6]
union, intersection = find_union_and_intersection(arr1, arr2)
print("Union:", union)
print("Intersection:", intersection)



def find_union_and_intersection_sorted(arr1, arr2):
    arr1.sort()
    arr2.sort()
    union = []
    intersection = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:
            union.append(arr1[i])
            intersection.append(arr1[i])
            i += 1
            j += 1

    # Add remaining elements
    while i < len(arr1):
        union.append(arr1[i])
        i += 1
    while j < len(arr2):
        union.append(arr2[j])
        j += 1

    return list(set(union)), intersection  # Ensure union has unique elements

# Example usage
arr1 = [1, 2, 2, 3, 4]
arr2 = [3, 4, 4, 5, 6]
union, intersection = find_union_and_intersection_sorted(arr1, arr2)
print("Union:", union)
print("Intersection:", intersection)
