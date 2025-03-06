# Longest Substring Without Repeating Characters

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# Examples
print(length_of_longest_substring("abcdxyzxb"))  # Output: 7
print(length_of_longest_substring("abcdabcbbxyzt"))  # Output: 5
print(length_of_longest_substring("pwwkew"))  # Output: 3


def subSG(s:str):
    subString = []
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if len(set(s[i:j])) == len(s[i:j]):
                subString.append(len(s[i:j]))
    return max(subString)
    
print(subSG("abcdxyzxb"))  # Output: 7
print(subSG("abcdabcbbxyzt"))  # Output: 5
print(subSG("pwwkew"))  # Output: 3