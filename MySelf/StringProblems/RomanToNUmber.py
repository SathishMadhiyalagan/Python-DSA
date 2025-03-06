# # Mapping of Roman numerals to integers
# roman_map = {
#     "I": 1,
#     "IV": 4,
#     "V": 5,
#     "IX": 9,
#     "X": 10,
#     "XL": 40,
#     "L": 50,
#     "XC": 90,
#     "C": 100,
#     "CD": 400,
#     "D": 500,
#     "CM": 900,
#     "M": 1000
# }

# def roman_to_int(roman):
#     i = 0
#     num = 0
#     while i < len(roman):
#         # Check if the next two characters form a valid Roman numeral (e.g., "IV", "CM")
#         if i + 1 < len(roman) and roman[i:i+2] in roman_map:
#             num += roman_map[roman[i:i+2]]
#             i += 2
#         else:
#             # Otherwise, add the value of the single character
#             num += roman_map[roman[i]]
#             i += 1
#     return num

# # Example usage
# roman = "MCMLXXXVII"  # 1987
# print(roman_to_int(roman))



def roman_to_integer(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

# Example usage
print(roman_to_integer("III"))    # Output: 3
print(roman_to_integer("IV"))     # Output: 4
print(roman_to_integer("LVIII"))  # Output: 58
print(roman_to_integer("MCMXCIV")) # Output: 1994
