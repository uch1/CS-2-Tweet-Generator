import random
import sys

def generate_random_sentence(words, word_count):
    '''
        This function will generate a random sentence once it is called
        Inputs:
            1. words(string): these are words that the user will enter as an input
            2. word_count(int): total count of words used in a sentenece
            example: "I love cookies"
        Output:
            example: "cookies I love", "I cookies cookies"
    '''
    sentence = ""
    random_words = random.choice(words)[:-1]

    for _ in range(word_count):
        sentence += random_words
    return sentence[:-1]

def main():
    '''
        Once this function is called,
    '''
    word_count = int(sys.argv[0])

    with open("/usr/share/dict/words") as filename:
        words = filename.readlines()

    return generate_random_sentence(words, word_count)

if __name__ == '__main__':
    print(main())
