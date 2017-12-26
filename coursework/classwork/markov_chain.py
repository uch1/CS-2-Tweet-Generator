from dictogram import Dictogram
import random


def first_order_markov_chain(word_list):
    '''
    Input:
    - word_list: words that will be used as an entry for the markov chain
      example: ['fish', 'red', 'fish', 'blue', 'fish', 'one', 'fish', two]
      index:   [  0       1       2       3       4       5      6      7]
                  cw      nw
    current_word(cw): current/first word in the word list
    next_word(nw): next_word/second word in the word list

    Output:
    - histogram = {
                    'fish'(cw): [{
                                'red'(nw): 1,
                                'blue'(nw): 1
                                }]
                }
    '''

    histogram = {}

    #1. iterate through the word list by index and get the current and next word
    for index in range(len(word_list) - 1):
        current_word = word_list[index]
        next_word = word_list[index + 1]
    #2. check if the word exist in the markov chain/histogram
        if current_word not in histogram:
            histogram[current_word] = Dictogram([next_word])
        else:
            histogram[current_word].add_count(next_word)

    return histogram


def second_order_markov_chain(word_list):
    histogram = {}

    for index in range(len(word_list) - 1):
        current_word = word_list[index]
        next_word = word_list[index + 1]
        after_next_word = word_list[index + 2]

        if (current_word, next_word) not in histogram:
            histogram[(current_word, next_word)] = Dictogram([after_next_word])
        else:
            histogram[(current_word, next_word)].add_count(after_next_word)

    return histogram

def nth_order_markov_chain(order, word_list):
    # histogram = {}
    #
    # for index in range(0, len(word_list) - order):
    #
    pass
