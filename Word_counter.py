#Liam Nagle-Cocco
#23 June 2017

#To count the recurrences of a word in a text file, case-sensitive.

def keyword_count(file_name, key_word):
    search_file = open(file_name)
    file_string = search_file.read()
    word_list = file_string.split()
    word_count = len(word_list)
    keywords = 0
    np_range = range(0,word_count,1)
    for i in np_range:
        if word_list[i]==key_word:
            keywords += 1
    search_file.seek(0)
    print """
The file contains %d words, of which %d are %s.
    """ % (word_count, keywords, key_word)
    print "Note this is case-sensitive. \n"
