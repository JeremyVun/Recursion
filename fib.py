import math

def fib(num):
  # Base cases
  if num <= 0:
    return 0
  elif num == 1:
    return 1
  else:
    return fib(num - 1) + fib(num - 2)


# tail recursion
def fib_tail(num, a=0, b=1):
  if num <= 0:
    return a
  elif num == 1:
    return b
  else:
    return fib_tail(num-1, b, a+b)


# Memoisation
def fib_iterative(num):
  # Base Cases
  fibs = {
    0: 0,
    1: 1
  }
  
  for i in range(num+1):
    if i not in fibs:
      fibs[i] = fibs[i - 1] + fibs[i - 2]
  
  return fibs[num]


# formula for num'th fibonacci number
# ( (sqrt(5) + 1)/2 )^(num) ) / sqrt(5)
def fib_math(n):
  res = (math.sqrt(5) + 1) / 2
  return round(pow(res, n) / math.sqrt(5))
