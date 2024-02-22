"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Kade Hemmerling
Lab Time: Thursday @ 2

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
    result = ''
    while user_num > 0:
        remainder = user_num % 2
        result += str(remainder)
        user_num //= 2
    print(result)
if __name__ == "__main__":
    reverse_binary()