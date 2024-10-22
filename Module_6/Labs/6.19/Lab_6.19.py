""" Type your code here. """


def replace_words():
    replacements = input().split()
    sentence = input()
    replace_dict = {}

    for i in range(0, len(replacements), 2):
        original_word = replacements[i]
        replacement_word = replacements[i + 1]
        replace_dict[original_word] = replacement_word

    sentence_words = sentence.split()
    updated_sentence = [replace_dict.get(word, word) for word in sentence_words]

    print(" ".join(updated_sentence))


replace_words()
