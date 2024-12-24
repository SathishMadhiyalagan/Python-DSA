# Python program to convert number into words by breaking 
# it into groups of three

def convertToWords(n):
    if n == 0:
        return "Zero"
    
    # Words for numbers 0 to 19
    units = [
        "",        "One",       "Two",      "Three",
        "Four",    "Five",      "Six",      "Seven",
        "Eight",   "Nine",      "Ten",      "Eleven",
        "Twelve",  "Thirteen",  "Fourteen", "Fifteen",
        "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ]
    
    # Words for numbers multiple of 10        
    tens = [
        "",     "",     "Twenty",  "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    ]
    
    multiplier = ["", "Thousand", "Million", "Billion"]
    
    res = ""
    group = 0
    
    # Process number in group of 1000s
    while n > 0:
        if n % 1000 != 0:
            
            value = n % 1000
            temp = ""
            
            # Handle 3 digit number
            if value >= 100:
                temp = units[value // 100] + " Hundred "
                value %= 100

            # Handle 2 digit number
            if value >= 20:
                temp += tens[value // 10] + " "
                value %= 10

            # Handle unit number
            if value > 0:
                temp += units[value] + " "

            # Add the multiplier according to the group
            temp += multiplier[group] + " "
            
            # Add the result of this group to overall result
            res = temp + res
        n //= 1000
        group += 1
    
    # Remove trailing space
    return res.strip()

if __name__ == "__main__":
    n = 214711
    print(convertToWords(n))