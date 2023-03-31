"""

Write a program whose input is two integers and whose output is the two integers swapped.

NOTE:
    I understand there are much simpler ways to accomplish this, but the lab needed the answer in a specific way
    most likely to add more of a challenge.
"""


def swap_values(user_val1, user_val2):
    # OUTPUT values in reverse order
    return (user_val2, user_val1)


if __name__ == '__main__':
    # INPUT two user entered values
    user_val1 = int(input())
    user_val2 = int(input())

    # SWAP the values
    user_val1, user_val2 = swap_values(user_val1, user_val2)
    # OUTPUT the values
    print(user_val1, user_val2)
