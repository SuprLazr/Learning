def search_phrase_file(file_name, search_phrase):
        test_doc = open(file_name)
        read_doc = test_doc.read()
        phrase_len = len(search_phrase)
        file_size = len(read_doc)
        x = 0
        if read_doc[x:(x+phrase_len)] == search_phrase:
                        return search_phrase
        while x < (file_size):
                if read_doc[x] == (','):
                        if read_doc[x+2:(x+phrase_len+2)] == search_phrase:
                                return search_phrase
                x += 1
        return 'Search phrase not found in file'

enter_file = input('Enter file address and name:')
enter_search_phrase = input('Enter search phrase: ')
print(search_phrase_file(enter_file, enter_search_phrase))


    