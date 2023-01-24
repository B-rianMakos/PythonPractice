import random
n=int(input("Enter a positive even integer for the size of the list?" ))

def loop():
    b = []
    for x in range(n):
        b.append(random.randint(1,100))
    print(b)
    newb = b[::2]
    print(newb)
loop()

