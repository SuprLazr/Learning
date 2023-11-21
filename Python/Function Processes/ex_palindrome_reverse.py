def palindrome(string):
    is_palindrome = False
    stringabc = string.isalpha()
    if stringabc is True:
        is_palindrome = True
        string_strip = string.strip()
        string_perfect = string_strip.lower()
        rev_string_perfect = list(reversed(string_perfect))
        x = 0
        len_string = len(string_perfect)
        while len_string / 2 >= 1:
            if rev_string_perfect[x] == string_perfect[x]:
                x +=1
                len_string = len_string-2
            else:
                is_palindrome = False
                break
    return is_palindrome

print(palindrome('racecar'))
print(palindrome('poop1'))