amount_to_change = int(input())

num_fives = amount_to_change // 5

''' Your solution goes here '''
num_ones = amount_to_change % 5

print('Change for $', amount_to_change)
print(num_fives, 'five dollar bill(s) and', num_ones, 'one dollar bill(s)')