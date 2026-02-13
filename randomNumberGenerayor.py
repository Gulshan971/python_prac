from random import randint
x = randint(1 , 6)
freq = 0 
while x != 1:
    x = x  / pow(x , x)
    freq += 1
    print(freq)
    print(f"x : {x}")
dir("random")