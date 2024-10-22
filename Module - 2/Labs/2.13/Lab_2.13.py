def count_character(string):
    character = string[0]
    phrase = string[1:].strip()

    # Count the occurrences of the character in the phrase.
    count = phrase.count(character)

    return count


# Get the input from the user.
input_string = input()

# Count the character occurrences and print the result.
count = count_character(input_string)
print(f"{count}")
