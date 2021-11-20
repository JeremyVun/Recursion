from measure import measure
from fib import fib, fib_tail, fib_iterative, fib_math

def main():
  while True:
    num = int(input("What fibonacci number do you want? "))
    choice = input("(r)ecursively, (t)ail recursively, (i)teratively or (m)athematically? ")

    if choice == "r":
      measure(fib, num)
    elif choice == "i":
      measure(fib_iterative, num)
    elif choice == "t":
      measure(fib_tail, num)
    elif choice == "m":
      measure(fib_math, num)
    

if __name__ == "__main__":
  main()