import random

def load_word():
    with open("words.txt", "r") as f:
        words = f.readlines()
        f.close()

def get_random_words(num):
    '''
    This function selects a
    random word from the txt file
    '''
    random_word = random.int(0, len(num))
#2 create a func generating setences using nums in a for loop in range(num)

def generate_sentence(num):
    '''
    Genrate a sentence by using a range of random numbers.
    '''

    sentence = []
    while num > len(sentence):
        
