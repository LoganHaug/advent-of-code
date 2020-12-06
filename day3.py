
with open('input/day3_input.txt') as input_file:
    map = [row.rstrip() for row in input_file]

def wrap(starting):
  while starting > len(map[0]) - 1:
    starting -= len(map[0])
  return starting

def calc_tree_hits(x_delta, y_delta):
  x_pos = 0
  tree_hit = 0
  i = 0
  while i < len(map)-1:
    if map[i][wrap(x_pos)] == '#':
      tree_hit += 1
    x_pos += x_delta
    x_pos = wrap(x_pos)
    i += y_delta
  if map[i][wrap(x_pos)] == '#':
      tree_hit += 1
  return tree_hit


print(f"Total for part 1: {calc_tree_hits(3, 1)}")
values = [(1,1), (3,1), (5,1), (7,1), (1,2)]
trees_hit = []
for value in values:
  trees_hit.append(calc_tree_hits(value[0], value[1]))
total = 1
for tree_path in trees_hit:
  total *= tree_path
print(f"Total for part 2: {total}")
