def word_frequencies():
    words = input().split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    for word in words:
        print(f'{word} {freq[word]}')


word_frequencies()