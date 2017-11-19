import sys, re, string



def load_file(source_file):
    with open("{}".format(source_file)) as f:
        loaded_file = f.readlines()


def clean_the_file(source_file):
    '''
    clean the text file by doing the following:
    1. remove whitespaces, new lines, tap spaces, punctuations
    2. lowercase the words
    '''
    #no_spaces = re.sub(pattern, repl, string, count=0, flags=0)
    removed_punc = ''.join([ char.lower() for char in filename
                            if char not in string.punctuation ])
    clean_file = re.split('\s*', removed_punc)[:-1]
    return clean_file

def unique_words(histogram):
    #returns the total count of unique words
    # word_count = len(histogram.keys())
    # return word_count
    word_count = 0
    # TODO: Optimize function using standard library
    # return len(histogram) more optimized solution
    for word in histogram:
        word_count += 1 # Refactor
    return word_count

def frequency(word, histogram):
    #returns the number of times that word appears in a text
    frequency = 0

    for each_word in histogram:
        if each_word == word:
            frequency = histogram[word]
    return frequency

def histogram_dict(source_file):
    #Output: histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}
    '''
    1. text_list: list
    2. dict that holds unique words(key) and num(value)
    3. iterate through file and add the words in a dict
    4. return histogram dictionary
    '''
    #word_count = 0
    histogram = {}
    # TODO: Fix function
    # TODO: Test solution
    # fish, red, fish, blue, hi
    for word in source_file:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
            # histogram[word] += 1 # Logical error
    return histogram

def histogram_list(source_file):
    #Output: histogram = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
    #TODO: Not completed
    temp_list = []
    histogram = []

    for word in source_file:
        if word not in histogram:


def histogram_tuples(source_file):
    #Output: histogram = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
    #TODO: Not completed
    histogram_tuple = [()]
    for key, value in source_file.items():

        histogram_tuple.append((key, value))
    return histogram_tuple

def generate_sentence(histogram, num_tokens, sentence_length):

def sample_by_frequency(histogram, frequency, num_tokens):
