import re
import random

def clean_data(source_file):
    '''
    Input:
    - source_file: string
    Process:
    - cleans the text file, removing everything except characters
    Output:
    - returns a random one word
    '''
    clean_file = re.sub('\s*\W*', '', source_file)

def get_random_word(histogram):
    '''
    Input:
    - histogram: dictionary
    Process:
    - Convert histogram from a dict to a list
    - Iterate and find a random word in the histogram
    Output:
    - Return a single word
    '''
    word_list = list(histogram)
    random_word = ' '

    while len(random_word) <= 0:

        random_index = random.randint(0, len(word_list) - 1)

        random_word = word_list[random_index]

    return random_word

def generate_sentence(histogram, num_tokens, sentence_length):
    '''
    Input:
    - histogram: dictionary
    - num_tokens: number of recurring words
    - sentence_length: Int
    Process:

    Output:
    '''
    word_list = list(histogram)

    sentence = " "

    while len(sentence_length) >= 0:

        random_index = random.randint(0, len(word_list) - 1)

        sentence.append(word_list[random_index])

        #words.pop(random_index)

    return sentence

def create_random_sentence(num, words):
    local_words = words
    final_word_list = []
    for _ in range(0, num):
        rand_index = random.randint(0, len(local_words) - 1)
        final_word_list.append(local_words[rand_index])
        local_words.pop(rand_index)

    return " ".join(final_word_list)

def sample_by_frequency(histogram, frequency, num_tokens):




if __name__ == '__main__':
    main()
