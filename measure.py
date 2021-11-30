######
# This module is used to graph the performance
# of different Fibonacci functions using matplotlib
# We use threading to make this faster
######

import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

import time
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor, as_completed

def measure(fib_func, n, runs=1):
  args = []
  for n in range(n + 1):
    args.append((fib_func, n, runs))

  # Schedule the tasks on our threads
  times = []
  with ThreadPoolExecutor(max_workers=n) as executor:
    for result in executor.map(measure_task, args):
      times.append(result)

  plot_graph(times)


# Individual task
def measure_task(args):
  fib_func = args[0]
  n = args[1]
  runs = args[2]

  # Measure the time to run the fib_function
  ts = time.time()
  result = fib_func(n)
  elapsed = time.time() - ts

  # Return measured time
  ms = elapsed * 1000 / runs
  print(f"{n}th Fibonacci is {result} \t({ms:.2f}ms)")

  return ms


# plot a 2d graph
def plot_graph(data):
  plt.rcParams["figure.figsize"] = (4, 2)
  plt.rcParams['toolbar'] = 'None'
  plt.plot(data)
  plt.pause(0.001)
