from random import shuffle
patte = ["diamond" , "king" , "queen"]
shuffle(patte)#It does not require any other variable/identifier as it has feature of in place shuffling
for card in patte:
    print(card)
