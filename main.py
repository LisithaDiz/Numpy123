from numpy import random

x = random.randint(100, size=(3, 5))
print(x)

x = random.rand(3,5)
print(x)

y = random.choice([3, 5, 7, 9])
print(y)

y = random.choice([3, 5, 7, 9], size=(3, 5))
print(y)
