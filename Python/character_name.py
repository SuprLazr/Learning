char_name = input('Enter Character Name: ')
if char_name.isalpha() == True:
    if len(char_name) >= 3:
        print(char_name,'accepted!')
    else:
        print('The character name must be at least three characters in length. Please try again.')
else:
    print('The character name cannot contain numbers, special characters, or spaces. Please try again.')



