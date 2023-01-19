import random
import string
print("\nGenerate a random color hex :")
print("#{:06x}".format(random.randint(0,0xFFFFFF)))
print("Generate a random alphabetical string:\n")
max_length = 255
s = ""
for i in range(random.randint(1, max_length)):
    s = s+random.choice(string.ascii_letters)
print(s)
print("Generate a random value between 0and 10, inclusive:")
print(random.randint(0, 10))
print("Generate a random value between -7 and 7, inclusive:")
print(random.randint(-7, 7))
print("Generate a random value between 1 and 1, inclusive:")
print(random.randint(1, 1))
print("Generate a random multiple of 7 between 0 and 70:")
print(random.randint(0,10)*7)
