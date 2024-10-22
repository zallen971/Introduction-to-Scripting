word = input()
password = ''

''' Type your code here. '''
replacements = {
    'i': '!',
    'a': '@',
    'm': 'M',
    'B': '8',
    'o': '.'
    }


for char in word:
    if char in replacements:
        password += replacements[char]
    else:
        password += char

password += 'q*s'
print(password)