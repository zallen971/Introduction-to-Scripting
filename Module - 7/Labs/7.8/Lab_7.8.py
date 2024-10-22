import csv

from collections import Counter


def count_word_frequencies(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        words = [word for row in reader for word in row]

        frequency = Counter(words)

        for word, count in frequency.items():
            print(f"{word} {count}")


if __name__ == "__main__":
    input_file = input()
    count_word_frequencies(input_file)