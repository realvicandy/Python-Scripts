"""

Write a program with total change amount as an integer input that outputs the change using the fewest coins, one coin
type per line. The coin types are dollars, quarters, dimes, nickels, and pennies. Use singular and plural coin names as
appropriate, like 1 penny vs. 2 pennies.

NOTE:
    This is similar to another lab I have already done. Except this one goes into a function.
NOTE:
    I'm sure there are other ways to do this, but the lab required an answer in this format

"""


def exact_change(user_total):
    # Evaluate currency
    dollars = user_total // 100
    quarters = user_total % 100 // 25
    dimes = user_total % 100 % 25 // 10
    nickels = user_total % 100 % 25 % 10 // 5
    pennies = user_total % 100 % 25 % 10 % 5 // 1
    return dollars, quarters, dimes, nickels, pennies


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    if input_val <= 0:
        print('no change')
    if input_val > 0:
        if num_dollars == 1:
            print(f'{num_dollars} dollar')
        elif num_dollars > 1:
            print(f'{num_dollars} dollars')

        if num_quarters == 1:
            print(f'{num_quarters} quarter')
        elif num_quarters > 1:
            print(f'{num_quarters} quarters')

        if num_dimes == 1:
            print(f'{num_dimes} dime')
        elif num_dimes > 1:
            print(f'{num_dimes} dimes')

        if num_nickels == 1:
            print(f'{num_nickels} nickel')
        elif num_nickels > 1:
            print(f'{num_nickels} nickels')

        if num_pennies == 1:
            print(f'{num_pennies} penny')
        elif num_pennies > 1:
            print(f'{num_pennies} pennies')
