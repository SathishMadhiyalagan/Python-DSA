def excel_column_to_number(column_name):
    column_number = 0
    for char in column_name:
        column_number = column_number * 26 + (ord(char.upper()) - ord('A') + 1)
    return column_number

# Examples
print(excel_column_to_number("A"))   # Output: 1
print(excel_column_to_number("AB"))  # Output: 28
print(excel_column_to_number("ABC")) # Output: 731
