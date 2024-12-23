number =111112

reNumStr = str(number)[::-1]

wordChrs = {
    0 : ["","one","two","three","four","five","six","seven","eight","nine"],
    1 : [["","ten","twenty","thirty","fouty","fifty","sixty","seventy","eighty","ninty"],["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]],
    2 : ["","hundred"],
    3 : ["","thousand"],
    4 : ["","lakh"],
    5 : ["","lakh"],
    6 : ["","crore"],
    7 : ["","crore"]
}

# print(number.split())

if number <=0:
    print("Zero")
else:
    words = []
    for i in range(len(str(number))):
        print(i,int(reNumStr[i]))
        # print(wordChrs[i][int(str(number)[i])])
        
        if i == 1 or i== 4 or i ==6:
            if int(reNumStr[i]) == 1 and int(reNumStr[i-1]) !=0:
                # print(wordChrs[i][1][int(reNumStr[i-1])])
                words.pop()
                # words.append(wordChrs[1][1][int(reNumStr[i-1])])
                if i== 4:
                    words.append(wordChrs[1][1][int(reNumStr[i-1])]+" "+(wordChrs[3][1]))
                elif i==6:
                    words.append(wordChrs[1][1][int(reNumStr[i-1])]+" "+(wordChrs[4][1]))
                else:
                    words.append(wordChrs[1][1][int(reNumStr[i-1])])
            else:
                # print(wordChrs[i][0][int(reNumStr[i])])
                words.append(wordChrs[1][0][int(reNumStr[i])])
                # if i== 4 or i ==6:
                #     words.append(wordChrs[1][0][int(reNumStr[i])])
                # else:
                #     words.append(wordChrs[1][0][int(reNumStr[i])])
        elif i == 0:
            words.append(wordChrs[0][int(reNumStr[i])])
        elif i== 2:
            if int(reNumStr[i]) == 0:
                # words.append( wordChrs[0][int(reNumStr[i])]+" "+ wordChrs[i][1] +" and" )
                # pass
                words.append("and" )
            else:
                if int(reNumStr[-1]) == 0:
                    words.append( wordChrs[0][int(reNumStr[i])]+" "+ wordChrs[i][1] +" and" )
                else:
                    words.append( wordChrs[0][int(reNumStr[i])]+" "+ wordChrs[i][1]  )
        else:
            # print(wordChrs[0][int(reNumStr[i])],wordChrs[i][1])
            words.append(wordChrs[0][int(reNumStr[i])]+" "+ wordChrs[i][1])

print(" ".join(words[::-1]))



number = 111112

# Dictionary for mapping digits and positions to words
wordChrs = {
    0: ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
    1: [["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"], 
        ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]],
    2: ["", "hundred"],
    3: ["", "thousand"],
    4: ["", "lakh"],
    6: ["", "crore"]
}

# Convert the number into a string and reverse it for easy indexing
reNumStr = str(number)[::-1]

if number <= 0:
    print("Zero")
else:
    words = []
    for i in range(len(str(number))):
        digit = int(reNumStr[i])

        # Handle "teens" (11-19)
        if i in [1, 4, 6] and digit == 1 and i - 1 >= 0 and int(reNumStr[i - 1]) != 0:
            # Remove the previous unit word and append the teen word
            words.pop()
            teen_word = wordChrs[1][1][int(reNumStr[i - 1])]
            position_word = wordChrs[i][1] if i in [4, 6] else ""
            words.append(teen_word + (" " + position_word if position_word else ""))
        else:
            # Handle other digits
            if i == 0 or i not in wordChrs:  # Units or unsupported positions
                words.append(wordChrs[0][digit])
            elif i == 2:  # Hundreds
                if digit != 0:
                    words.append(wordChrs[0][digit] + " " + wordChrs[i][1])
            elif i in wordChrs:  # Thousands, Lakhs, Crores
                if digit != 0:
                    words.append(wordChrs[0][digit] + " " + wordChrs[i][1])
                elif i - 1 >= 0 and int(reNumStr[i - 1]) != 0:  # Handle cases like "01 thousand"
                    words.append(wordChrs[i][1])

    print(" ".join(words[::-1]))

    