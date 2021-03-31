# Exercise Two
# Write a simple program that finds the value at the nth position in the Fibonacci sequence

def fibonacci(n):
    
    if n <= 2:
        print("IF: " + str(n))
        return 1
    else:
        print("ELSE: " + str(n))
        return fibonacci(n-1) + fibonacci(n-2)
        
x = fibonacci(0)
print(x)
