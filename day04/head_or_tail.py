import random


number_0_or_1 =round(random.random())

if number_0_or_1 == 0:
    print("Head")
else:
    print("Tail")

# or use randint()

random_int_number = random.randint(0, 1)

if random_int_number == 0:
    print("Heads")
else:
    print("Tails")