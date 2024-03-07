

import time

def speed_calc_decorator(func):
  def wrapper():
    start_time = time.time()
    func()
    new_time = time.time()
    time_dif = new_time - start_time
    print(f'{func.__name__} run spd: {time_dif} sec')

  return wrapper


@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i


@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i


fast_function()
slow_function()