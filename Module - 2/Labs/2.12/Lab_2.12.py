# Get the input from the user with a prompt message
name = input()

first_initial = name.split()[0][0]
middle_initial = name.split()[1][0]

if len(name.split()) == 2:
    first_name, last_name = name.split()
    formatted_name = f'{last_name}, {first_initial}.'
else:
    first_name, middle_name, last_name = name.split()
    formatted_name = f'{last_name}, {first_initial}.{middle_initial}.'

print(formatted_name)