"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Kade Hemmerling
Lab Time: Thursday @ 2
"""

def norm():
    # Write your code here
    num_values = int(input())
    values = [float(input()) for _ in range(num_values)]
    max_value = max(values)
    
    for value in values:
        normalized_value = value / max_value
        
    
    print(f'{normalized_value:.2f}')

if __name__ == "__main__":
    norm()