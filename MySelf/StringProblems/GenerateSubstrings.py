def generate_substrings(s: str):
    substrings = []
    for i in range(len(s)):  # Start index of substring
        for j in range(i + 1, len(s) + 1):  # End index (exclusive)
            substrings.append(s[i:j])  # Append the substring
    return substrings

# Example usage
s = "abcdxyzxb"
result = generate_substrings(s)
print(result)
