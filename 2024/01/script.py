

SHORT = "./short.txt"
INPUT = "./input.txt"

left_list = []
right_list = []

# with open(SHORT) as f:
with open(INPUT) as f:
  for line in f:
    line = line.strip()
    tb = [int(i) for i in line.split()]
    left_list.append(tb[0])
    right_list.append(tb[1])



# print(left_list)
# print(right_list)

# Part one : brute force
left_list.sort()
right_list.sort()

# print("left_list", left_list)
# print("right_list", right_list)


sum_diff = 0
for i in range(len(left_list)):
  sum_diff += abs(left_list[i] - right_list[i])

print("Sum of diffs :", sum_diff)  # 2166959


# Part two : use the sorted lists
similarity = 0
right_cursor = 0


LEN_LISTS = len(left_list)

for i in range(LEN_LISTS):
  item = left_list[i]
  item_score = 1
  occurrences_in_left = 0

  while right_list[right_cursor] < item:
    right_cursor += 1
  
  # print(item, item_score, right_cursor)
  if right_list[right_cursor] != item:
    continue

  while i < LEN_LISTS and left_list[i] == item:
    i += 1
    occurrences_in_left += 1
    # print("iiiiii", i)
  # print("matched", item, "at", right_cursor)
  right_cursor += 1

  while right_list[right_cursor] == item:
    right_cursor += 1
    item_score += 1
  # print(item_score, right_cursor)
  similarity += item_score * item * occurrences_in_left
print("similarity", similarity)
