def power_of(a, b):
  if b == 0:
    return 1
  return power_of(a, b-1) * 2


def main():
  # 2^5
  result = power_of(2, 5)
  print(result)


######
# Entry point
######
if __name__ == "__main__":
  main()