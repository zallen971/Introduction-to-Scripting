# get 3 int inputs from user
num_one = int(input())
num_two = int(input())
num_three = int(input())

# create smalles num variable and make it empty
smallest_num = ''

# if statements to determine smallest number of the 3 ints
if num_one <= num_two and num_one <= num_three:
    smallest_num = num_one
elif num_two <= num_one and num_two <= num_three:
    smallest_num = num_two
else:
    smallest_num = num_three

print(smallest_num)
