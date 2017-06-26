#Liam Nagle-Cocco
#Original: 23 June 2017
#Version 2.0: 26 June 2017. Changed to make case-insensitive and ignore full stops and commas.

#To count the recurrences of a word in a text file, case-insensitive.

def keyword_count(file_name, key_word):
    search_file = open(file_name)
    file_string = search_file.read()
    word_list = file_string.split()
    word_count = len(word_list)
    upper_case = ['A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(0,word_count):
        letters = list(word_list[i])
        word_list[i] = ''
        for j in range(0,len(letters)):
            for k in range(0,len(upper_case)):
                if str(letters[j]) == str(upper_case[k]):
                    letters[j] = lower_case[k]
                elif (str(letters[j]) =='.') or (str(letters[j]) ==','):
                    letters[j]=''
            word_list[i] += letters[j]
    letters2 = list(key_word)
    key_word2 = ''
    for i in range(0,len(letters2)):
        for j in range(0,len(upper_case)):
            if str(letters2[i]) == str(upper_case[j]):
                letters2[i] = lower_case[j]
        key_word2 += str(letters2[i])
    keywords = 0
    np_range = range(0,word_count,1)
    for i in np_range:
        if word_list[i]==key_word2:
            keywords += 1
    search_file.seek(0)
    print """
The file contains %d words, of which %d are %r.
    """ % (word_count, keywords, key_word2)
