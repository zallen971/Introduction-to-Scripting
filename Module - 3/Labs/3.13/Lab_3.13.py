"""
Write a program with total change amount as an integer input,
and output the change using the fewest coins, one coin type per line.
The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies.
Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.
"""


def get_coin_name(coin, count):
    if count == 1:
        return f"{count} {coin}"
    elif coin == "Penny":
        return f"{count} Pennies"
    else:
        return f"{count} {coin}s"


# get total change input
total_change = int(input())

# define coin values
if total_change == 0:
    print('No change')
else:
    dollar = 100
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

#calculate the number of each coin
dollars = total_change // dollar
total_change %= dollar

quarters = total_change // quarter
total_change %= quarter

dimes = total_change // dime
total_change %= dime

nickels = total_change // nickel
total_change %= nickel

pennies = total_change // penny
total_change %= penny

# Output results
if dollars > 0:
    print(get_coin_name("Dollar", dollars))
if quarters > 0:
    print(get_coin_name("Quarter", quarters))
if dimes > 0:
    print(get_coin_name("Dime", dimes))
if nickels > 0:
    print(get_coin_name("Nickel", nickels))
if pennies > 0:
    print(get_coin_name("Penny", pennies))
