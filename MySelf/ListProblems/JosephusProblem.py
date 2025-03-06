def josephus_problem(lst, step):
    index = 0  # Starting index
    while len(lst) > 1:
        index = (index + step - 1) % len(lst)  # Circular index calculation
        print(f"Removing: {lst[index]}")
        lst.pop(index)  # Remove element at index
    return lst[0]  # Return the last remaining element

list1 = ["A", "B", "C", "D", "E", "F", "G"]
final_value = josephus_problem(list1, 3)

print("Final remaining element:", final_value)



list1 = ["A", "B", "C", "D", "E", "F", "G"]
step = 3
index = 0  # Starting index
while len(list1) > 1:
    index = (index + step - 1) % len(list1)  # Circular index calculation
    list1.pop(index)  # Remove element at index
      # Return the last remaining element




print("Final remaining element:", list1)
