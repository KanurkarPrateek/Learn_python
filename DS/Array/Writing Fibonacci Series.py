fib = [0,1]
n = int(input("enter a number"))

for i in range(n):
    fib.append(fib[-1]+fib[-2])