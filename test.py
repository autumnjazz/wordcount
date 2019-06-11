full_text = """"The time has come," the Walrus said, "To talk of many things: Of shoes--and ships--and sealing-wax-- Of cabbages--and kings-- And why the sea is boiling hot-- """
    word_list = full_text.lower().split()
    notchar_list = []
    modified = []
    word_dictionary = {}

    for i in range(32, 127):
        if(64<i<91 or 96<i<123):
            pass
        else:
            notchar_list.append(chr(i))
    
    for word in word_list:
        for nchar in notchar_list:
            while (nchar in word):
                modified.append(word.replace(nchar,""))

    
    for word in modified:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    ordered = sorted(word_dictionary.items(), key=lambda t : t[1])

    print(ordered)