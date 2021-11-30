######
# This module is used to graph the performance
# of different Fibonacci functions using matplotlib
# We use threading to make this faster
######

import time
import matplotlib.pyplot as plt

def measure(fib_func, fib_num, runs=1):
  # Schedule the tasks on our threads
  futures = []
  with ThreadPoolExecutor(max_workers=fib_num) as executor:
    for n in range(fib_num + 1):
      futures.append(executor.submit(measure_task, fib_func, n))

  # Get the time results
  times = []
  for future in as_completed(futures):
    times.append(future.result())

  plot_graph(times)


# Individual task
def measure_task(fib_func, fib_num):
  # Measure the time to run the fib_function
  ts = time.time()
  result = fib_func(n)
  total_time += time.time() - ts

  # Return measured time
  ms = total_time * 1000 / runs
  print(f"{n}th Fibonacci is {result} \t({ms:.2f}ms)")

  return ms


# plot a 2d graph
def plot_graph(data):
  plt.rcParams["figure.figsize"] = (6, 3)
  plt.rcParams['toolbar'] = 'None'
  plt.plot(data)
  plt.pause(0.001)
