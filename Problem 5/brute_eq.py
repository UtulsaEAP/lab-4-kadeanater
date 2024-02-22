"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: kade Hemmerling
Lab Time: Thursday @ 2
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())

    # YOUR CODE HERE
    for x in range(-10 , 10):
        for y in range(-10 , 10):
            if a * x + b * y == c and d * x + e * y == f:
                print (f'x = {x} , y = {y}')
                
    else:
        print('There is no solution')
    
    
    
    
        
if __name__ == "__main__":
    brute_eq()