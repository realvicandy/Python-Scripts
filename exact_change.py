# Write a program with total change amount as an integer input, and output the change using the fewest coins,
# one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies.
# Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

total_change = int(input())

# Evaluate currency
dollars = total_change // 100
quarters = total_change % 100 // 25
dimes = total_change % 100 % 25 // 10
nickels = total_change % 100 % 25 % 10 // 5
pennies = total_change % 100 % 25 % 10 % 5 // 1

if total_change == 0:
    print('No change')

if dollars == 1:
    print(f'{dollars} Dollar')
elif dollars > 1:
    print(f'{dollars} Dollars')

if quarters == 1:
    print(f'{quarters} Quarter')
elif quarters > 1:
    print(f'{quarters} Quarters')

if dimes == 1:
    print(f'{dimes} Dime')
elif dimes > 1:
    print(f'{dimes} Dimes')

if nickels == 1:
    print(f'{nickels} Nickel')
elif nickels > 1:
    print(f'{nickels} Nickels')

if pennies == 1:
    print(f'{pennies} Penny')
elif pennies > 1:
    print(f'{pennies} Pennies')
