import itertools
import math
n = 102123161417560384731360000
a = itertools.combinations(range(int(math.sqrt(n))+1), 1)
for i in a:
    print(i)
