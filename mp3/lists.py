import random

print(sorted([i for i in random.sample(range(1,50), 20) if i in random.sample(range(1,50), 30)]))