# FIXME (1): Finish reading another word and an integer into variables.
# Output all the values on a single line
favorite_color = input()
favorite_word = input()
favorite_num = int(input())

print(f'You entered: {favorite_color} {favorite_word} {favorite_num}')


# FIXME (2): Output two password options
password1 = f'{favorite_color}_{favorite_word}'
password2 = f'{favorite_num}{favorite_color}{favorite_num}'
print(f'\nFirst password: {password1}')
print(f'Second password: {password2}')


# FIXME (3): Output the length of the two password options
pass1_length = len(password1)
pass2_length = len(password2)
print(f'\nNumber of characters in {password1}: {pass1_length}')
print(f'Number of characters in {password2}: {pass2_length}')