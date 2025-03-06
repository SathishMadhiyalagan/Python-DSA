def longest_palindromic_substring(s):
    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        odd = expand_from_center(i, i)
        even = expand_from_center(i, i + 1)
        longest = max(longest, odd, even, key=len)
    return longest


print(longest_palindromic_substring("babaad"))