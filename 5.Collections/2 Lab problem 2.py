import string


def add_word(word, word_set):
    # if word:
    #     word_set.add(word)
    word_set.add(word)


def process_line(line, word_set):
    line = line.strip()
    words = line.split(" ")
    for word in words:
        word = word.lower()
        word = word.strip()
        word = word.strip(string.punctuation)
        add_word(word, word_set)


def read_file(filename, word_set):
    gba_file = open(filename, 'r')
    for line in gba_file:
        process_line(line, word_set)


def main():
    word_set1 = set()
    word_set2 = set()

    read_file('test1.txt', word_set1)
    read_file('test2.txt', word_set2)

    print("Common words: ", word_set1.intersection(word_set2))
    print("Unique words: ", word_set1.symmetric_difference(word_set2))
    print("Test 1 exclusive words: ", word_set1.difference(word_set2))
    print("Test 2 exclusive words: ", word_set2.difference(word_set1))


main()
