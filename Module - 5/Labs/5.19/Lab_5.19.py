# Define your function here
def exact_change(user_total):
    num_dollars = user_total // 100
    user_total %= 100

    num_quarters = user_total // 25
    user_total %= 25

    num_dimes = user_total // 10
    user_total %= 10

    num_nickels = user_total // 5
    user_total %= 5

    num_pennies = user_total
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    user_total = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(user_total)

    # Type your code here.
    if user_total <= 0:
        print('no change')
    else:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(user_total)

        if num_dollars > 0:
            print(num_dollars, 'dollar' if num_dollars == 1 else 'dollars')
        if num_quarters > 0:
            print(num_quarters, 'quarter' if num_quarters == 1 else 'quarters')
        if num_dimes > 0:
            print(num_dimes, 'dime' if num_dimes == 1 else 'dimes')
        if num_nickels > 0:
            print(num_nickels, 'nickel' if num_nickels == 1 else 'nickels')
        if num_pennies > 0:
            print(num_pennies, 'penny' if num_pennies == 1 else 'pennies')