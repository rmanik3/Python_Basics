#Fibanacii Series

# Enter input from Stdin (Manual Entry)
n=int(input("Please enter the max value for the Fibonocci series"))

def fib(n):
    a,b = 1,0
    while a < n:
          print(a)
          a,b = a+b, a

fib(n)

          
