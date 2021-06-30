from itertools import permutations

a = input()

print([''.join(a) for a in permutations('dune')])
