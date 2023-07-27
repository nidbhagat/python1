from functools import reduce
def func(integers, names, numbers):
  '''
  input:
  integers -> list of integers to perform the square operation on
  names -> list of names to filter out as per the condition
  numbers -> list of numbers whose product we want

  output:
  map_result -> output of integers list
  filter_result -> output of the names list
  reduce_result -> output of the numbers list
  '''
  map_result, filter_result, reduce_result = None, None, None

  integers = [int(num) for num in input("in1:").split(" ")]
  names = input("in2:").split(" ")
  numbers = [int(num) for num in input("in3:").split(" ")]

  map_result = list(map(lambda x: x ** 2, integers))
  filter_result = list(filter(lambda x: len(x) <= 7, names))
  reduce_result = reduce(lambda x, y: x * y, numbers)

  return map_result, filter_result, reduce_result

print(func(None, None, None))
