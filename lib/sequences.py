#!/usr/bin/env python3

def print_fibonacci(length):
  fib_list = []
  a, b = 0, 1
  
  for _ in range(length):
      fib_list.append(a)
      a, b = b, a + b
  
  
  #fib_list.append(0)
  print(fib_list)
  
  
  
