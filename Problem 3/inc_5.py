"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Kade Hemmerling
Lab Time: Thursday @ 2
"""

def inc_5():
    # Write your code here
    initial_value = int(input())
    final_value = int(input())
    
    if final_value < initial_value:
        print("Second integer can't be less than the first.")
        return
    current_value = initial_value
    while current_value <= final_value:
    
        print(current_value)
        current_value += 5

if __name__ == '__main__':
    inc_5()