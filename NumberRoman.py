# Python implementation

arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_map = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M"
}

def int_to_roman(num):
    ans = ""
    for value in arr:
        if num >= value:
            q = num // value
            num = num % value

            for _ in range(q):
                ans += roman_map[value]
    return ans

# Example usage
num = 19
print(int_to_roman(num))
