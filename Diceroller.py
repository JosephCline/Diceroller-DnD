import random
diceroll = input("Please enter which dice you wish to roll, d4,d6,d8,d10,d12,d20 \n")
diceroll_4 = [1, 2 ,3 ,4]
diceroll_6 = [1, 2 ,3 ,4, 5, 6]
diceroll_8 = [1, 2 ,3 ,4, 5, 6, 7, 8]
diceroll_10 = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10]
diceroll_12 = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10, 11, 12]
diceroll_20 = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

d4 = random.choice(diceroll_4)
d6 = random.choice(diceroll_6)
d8 = random.choice(diceroll_8)
d10 = random.choice(diceroll_10)
d12 = random.choice(diceroll_12)
d20 = random.choice(diceroll_20)

if diceroll == "d4":
    print(d4)
elif diceroll == "d6":
    print(d6)
elif diceroll == "d8":
    print(d8)
elif diceroll == "d10":
    print(d10)
elif diceroll == "d12":
    print(d12)
elif diceroll == "d20":
    print(d20)
