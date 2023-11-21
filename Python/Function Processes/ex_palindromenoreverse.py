def palindrome(string):
    Teststring = string.strip()
    stringabc = Teststring.isalpha()
    if stringabc is False:
        return False
        #this part checks if the string has no numbers
    TestStringNoSpaces = Teststring.lower()
    #removes spaces - not sure if this part is necessary
    lenpal = len(TestStringNoSpaces)
    #set up line to run our while loop
    if len(TestStringNoSpaces) % 2 == 0:
        #even number amount of letters - modulo operator!!
        while lenpal > 0:
            if TestStringNoSpaces[0] == TestStringNoSpaces[-1]:
                pass
            else:
                return False
            lenpal = lenpal - 2
            if lenpal > 0:
                pass
            else:
                break
            #this is the only way I've found for the while loop to check the criteria while it iterates
            if TestStringNoSpaces[1] == TestStringNoSpaces[-2]:
                pass 
            else:
                return False
            lenpal = lenpal - 2
            if lenpal > 0:
                pass
            else:
                break
            if TestStringNoSpaces[2] == TestStringNoSpaces[-3]:
                pass
            else:
                return False
            lenpal = lenpal - 2
            if lenpal > 0:
                pass
            else:
                break
            if TestStringNoSpaces[3] == TestStringNoSpaces[-4]:
                pass
            else:
                return False
            lenpal = lenpal - 2
            if lenpal > 0:
                pass
            else:
                break
            if TestStringNoSpaces[4] == TestStringNoSpaces[-5]:
                pass
            else:
                return False
            if TestStringNoSpaces[5] == TestStringNoSpaces[-6]:
                pass
            else:
                return False
            lenpal = lenpal - 2
            if lenpal > 0:
                pass
            else:
                break
        return True   
    elif len(TestStringNoSpaces) % 2 == 1:
        while lenpal > 1:
            if TestStringNoSpaces[0] == TestStringNoSpaces[-1]:
                pass
            else:
                return False
            lenpal = lenpal - 2
            if lenpal > 1:
                pass
            else:
                break
            if TestStringNoSpaces[1] == TestStringNoSpaces[-2]:
                pass 
            else:
                return False
            lenpal = lenpal - 2
            if lenpal > 1:
                pass
            else:
                break
            if TestStringNoSpaces[2] == TestStringNoSpaces[-3]:
                pass
            else:
                return False
            lenpal = lenpal - 2
            if lenpal > 1:
                pass
            else:
                break
            if TestStringNoSpaces[3] == TestStringNoSpaces[-4]:
                pass
            else:
                return False
            lenpal = lenpal - 2
            if lenpal > 1:
                pass
            else:
                break
            if TestStringNoSpaces[4] == TestStringNoSpaces[-5]:
                pass
            else:
                return False
            if TestStringNoSpaces[5] == TestStringNoSpaces[-6]:
                pass
            else:
                return False
            lenpal = lenpal - 2
            if lenpal > 1:
                pass
            else:
                break
        return True

print(palindrome('ps')) 
