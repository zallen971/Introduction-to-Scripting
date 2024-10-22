while True:
    user_input = input()
    word, number = user_input.split()

    if word == 'quit':
        break

    print(f'Eating {number} {word} a day keeps the doctor away.')