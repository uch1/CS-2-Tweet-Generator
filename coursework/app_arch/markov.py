import random


def get_histogram(word_list):
    # Output: { fish: { blue: 1, red: 1, two: 1 }, blue: {'fish': 1} }
    histogram = {}

    for index, word in enumerate(word_list):

        if index == len(word_list) - 1:
            break

        next_word = word_list[index + 1]
        if word not in histogram:
            histogram[word] = {next_word: 1}
        else:
            if next_word not in histogram[word]:
                histogram[word][next_word] = 1
            else:
                histogram[word][next_word] += 1

    return histogram

def generate_sentence(sentence_length, histogram):
    pass

word_list = ['one','fish', 'two', 'fish', 'blue', 'fish', 'red', 'fish', 'house','fish', 'house', 'strawberry']

result = get_histogram(word_list)
print(result)
