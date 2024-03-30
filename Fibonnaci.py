def fibonacci(n):
    fib_series = [0, 1]  # Initialize with the first two Fibonacci numbers
    for i in range(2, n):
        next_num = fib_series[-1] + fib_series[-2]  # Calculate the next Fibonacci number
        fib_series.append(next_num)
    return fib_series[:n]  # Return the first n Fibonacci numbers

# Example usage:
n = 10  # Number of Fibonacci numbers to generate
print(fibonacci(n))
