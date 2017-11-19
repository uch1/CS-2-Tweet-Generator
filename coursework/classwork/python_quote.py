#example
import random

def load_random_words():
    with open("words.txt", "r") as f:
        words = f.readlines()
        random_words = random.choice(words)
    return get_random_words(random_words)

def get_random_words():
    lst = []
    rand_index = random.randint(0, len(quotes) - 1)
    for word in rand
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
