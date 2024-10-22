''' Define your function here. '''


def swap_values(user_val1, user_val2):
    return user_val2, user_val1


if __name__ == '__main__':
    ''' Type your code here. Your code must call the function. '''
    user_val1 = int(input())
    user_val2 = int(input())

    swapped_val1, swapped_val2 = swap_values(user_val1, user_val2)

    print(swapped_val1, swapped_val2)