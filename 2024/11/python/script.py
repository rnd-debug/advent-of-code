
from typing import List, Tuple, Callable, Dict

SHORT = "./short.txt"
INPUT = "./input.txt"

initial_tb_of_tuples: List[Tuple[str, int]] = []

type Tutuple = Tuple[str, int]


def rule_0(t: Tutuple) -> List[Tutuple]:
  if t[1] == 0:
    return True
  else:
    return False
  
def treatment_0(t: Tutuple) -> List[Tutuple]:
  return [("1", 1)]

def rule_split(t: Tutuple) -> List[Tutuple]:
  if len(t[0]) % 2 == 0:
    return True
  else:
    return False
  
def string_to_tuple(s: str) -> Tutuple:
  nb = int(s)
  new_s = str(nb)
  return (new_s, nb)

def treatment_split(t: Tutuple) -> List[Tutuple]:
  right = t[0][len(t[0])//2:]
  left = t[0][:len(t[0])//2]
  return [string_to_tuple(left), string_to_tuple(right)]

  
def rule_2024(t: Tutuple) -> List[Tutuple]:
  return True

def treatment_2024(t: Tutuple) -> List[Tutuple]:
  m = t[1] * 2024
  return [(str(m), m)]


# with open(SHORT) as f:
with open(INPUT) as f:
  for line in f:
    line = line.strip()
    tb = line.split()
    initial_tb_of_tuples = list(map(lambda x: (x, int(x)), tb))

functions = [(rule_0, treatment_0), (rule_split, treatment_split), (rule_2024, treatment_2024)]

NB_ITERATIONS = 25

# Round one
def process_one_tuple(t: Tutuple) -> List[Tutuple]:
  for (rule, fct) in functions:
    if rule(t):
      return fct(t)
  return None # should not happen

tb_of_tuples = initial_tb_of_tuples
for i in range(NB_ITERATIONS):
  result = []
  for t in tb_of_tuples:
    result.extend(process_one_tuple(t))
  tb_of_tuples = result

print(len(tb_of_tuples)) # 220722

#####################################################
# Round two - brute force. This will be killed by OOM
# tb_of_tuples = initial_tb_of_tuples

# def flatten_extend(matrix):
#   flat_list = []
#   for row in matrix:
#       flat_list.extend(row)
#   return flat_list

# from multiprocessing import Pool
# import tracemalloc
# tracemalloc.start()

# NB_ITERATIONS = 75
# for i in range(NB_ITERATIONS):
#   with Pool() as P:
#     xtransList = P.map(process_one_tuple, tb_of_tuples)
#     tb_of_tuples = flatten_extend(xtransList)

#   print(tracemalloc.get_traced_memory()[0] / 1024)

# # stopping the library
# tracemalloc.stop()
# print(len(tb_of_tuples)) 

#####################################################

NB_ITERATIONS = 75
dict_of_ints : Dict[int, int] = {}

for t in initial_tb_of_tuples:
  if t[1] in dict_of_ints:
    dict_of_ints[t[1]] += 1
  else:
    dict_of_ints[t[1]] = 1

for i in range(NB_ITERATIONS):
  result : Dict[int, int] = {}

  for (k, nb_occurrences) in dict_of_ints.items():
    list_next_tuples = process_one_tuple((str(k), k))
    for t in list_next_tuples:
      if t[1] in result:
        result[t[1]] += nb_occurrences
      else:
        result[t[1]] = nb_occurrences

  dict_of_ints = result

from functools import reduce

print(reduce(lambda x, y: x + y, dict_of_ints.values(), 0)) # 261952051690787