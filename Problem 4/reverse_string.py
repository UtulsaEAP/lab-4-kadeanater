"""
Complete the following python code to reverse the string entered by the user.

Name: Kade Hemmerling
Lab Time: Thursday @ 2
"""

def reverse_string():
    # YOUR CODE HERE
    user_input= input()
    reverse = user_input[::-1]
    print(reverse)

if __name__ == "__main__":
    reverse_string()