def palindrome(string):
    return string[::-1] == string
#[::-1] converts to [start:stop:step] or [0:len(string):-1]

print(palindrome('racecar1'))