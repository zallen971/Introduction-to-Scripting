triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

for i in range(1, triangle_height + 1):
    for j in range(i):
        print(triangle_char, end=' ')
    print()