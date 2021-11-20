import time
import matplotlib.pyplot as plt


def measure(func, arg, runs=1):
  times = []

  for n in range(arg+1):
    total_time = 0
    for i in range(runs):
      ts = time.time()
      result = func(n)
      total_time += time.time() - ts

    ms = total_time * 1000 / runs
    times.append(ms)
    print(f"{n}th Fibonacci is {result} \t({ms:.2f}ms)")

  plot_graph(times)


# plot a 2d graph
def plot_graph(data):
  plt.rcParams["figure.figsize"] = (6, 3)
  plt.rcParams['toolbar'] = 'None'
  plt.plot(data)
  plt.pause(0.001)
