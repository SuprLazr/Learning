string_phrase = 'with three words'
abcgo = string_phrase + ' '
x = 0
abclist = list()
for letter in abcgo:
    if letter == ' ' and len(abclist)<1: 
        word = (abcgo[:x])
        abclist[len(abclist):] = [word]
        buffer = (abcgo[:x])
        int_buffer = len(buffer)
    elif letter == ' ' and len(abclist) >= 1:
        word = (abcgo[int_buffer+1:x])
        abclist[len(abclist):] = [word]
        buffer = (abcgo[:x])
        int_buffer = len(buffer)
    x+=1
print(abclist)