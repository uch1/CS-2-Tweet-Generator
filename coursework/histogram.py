import sys, re, string


def clean_the_file(filename):
    '''
    clean the text file by doing the following:
    1. remove whitespaces, new lines, tap spaces, punctuations
    2. lowercase the words
    '''
    no_spaces = re.sub(pattern, repl, string, count=0, flags=0)
    removed_punc = ''.join([ char.lower() for char in filename
                            if char not in string.punctuation ])
    clean_file = re.split('\s*', removed_punc)[:-1]
    return clean_file

def histogram_dict(text_file):
    '''
    1. text_list: list
    2. dict that holds unique words(key) and num(value)
    3. iterate through file and add the words in a dict
    4. return histogram dictionary
    '''
    word_count = 0
    histogram = {}

    for word in text_file:
        if word not in histogram:
            histogram[word] += 1
    return histogram
