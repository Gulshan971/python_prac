import random 
coin = random.choice(["head" , "tail"])
x = 0 
chance = 0 
while coin != "tail":
     coin = random.choice(["head" , "tail"])
     x  = x + 1
     chance = chance + 1
try:     
    prob = x / chance 
except ZeroDivisionError :
     pass
else:  print(prob)   
     
