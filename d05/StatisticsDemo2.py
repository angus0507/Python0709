import statistics
import random

def getStat(list):
    list.sort()
    mean = statistics.mean(list)
    stdev = statistics.stdev(list)
    cv = stdev / mean
    return mean, stdev, cv

a, b = [], []
for i in range(0, 10):
    a.append(random.randint(0, 10))
    b.append(random.randint(0, 10))

print(a)
print(b)

