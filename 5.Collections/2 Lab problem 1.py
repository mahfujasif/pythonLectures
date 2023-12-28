import string


def add_word(word, word_count_dict):
    if word:
        count = word_count_dict.get(word, 0)
        count = count + 1
        word_count_dict[word] = count


def process_line(line, word_count_dict):
    line = line.strip()
    words = line.split(" ")
    for word in words:
        word = word.lower()
        word = word.strip()
        word = word.strip(string.punctuation)
        add_word(word, word_count_dict)


def main():
    word_count_dict = {}
    gba_file = open('test2.txt', 'r')
    for line in gba_file:
        process_line(line, word_count_dict)
    print('Length of the dictionary:', len(word_count_dict))
    print(word_count_dict)


main()
