from random import choice
y = 0 
total = 1
while True:
      x = choice(["head" , "tail"])
      print(x)
      if x == "tail":
         break
      else :
           y = y + 1
           print(f"Probability: {y/total}")
           total += 1
      
      