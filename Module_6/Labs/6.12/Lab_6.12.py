''' Type your code here. '''
user_input = input()

numbers = list(map(int, user_input.split()))

average = sum(numbers) / len(numbers)

max_value = max(numbers)

print(int(average), max_value)