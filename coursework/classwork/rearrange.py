import random
import sys

def rearrange_words(words_list):
    rearranged_words = []

    for word in range(0, len(words_list)):
        rand_num = random.randint(0, len(word) - 1)
        pop_word = words_list.pop(rand_num)
        rearrange_words.append(pop_word)
    return " ".join(words_list)

if __name__ == "__main__":
    args = sys.argv[1:]
    print(rearrange_words(args))
