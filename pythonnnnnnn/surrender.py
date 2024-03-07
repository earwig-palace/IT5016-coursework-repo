# fuckin around with loops
for x in range(4, 8, 2):
    print(x)
# heyyyy! it works!
inv = ["key", "potion1", "potion2", "dagger", "meat"]
for item in inv:
    print(item)
# ok cool
gay = int(input("how many times should i say some gay shit > "))
for bleh in range(gay):
    print("an army of lovers cannot lose ;)", bleh)
# now some while loops!
number = int(input("ok give me a number..  "))
while number != 24:
    print(number, "is a bad number! try again dipshit!!")
    number = int(input("ok give me a number but this time make it good..  "))
print("FINALLY. you got it.")
# hehehehe
n = 0
while n < 10:
    print(n)
    n = n + 1
# im actually not very good at commenting my code :(
space = ["hallway", "stairwell", "elevator", "breakroom", "office"]
element = ["miserable", "decaying", "filthy", "garbage-choked", "overgrown"]
for i in space:
    for j in element:
        print(j, i)
# i'm starting to see the utility of all this! i nneed 2 practise more thooo lol
# i really wanna know how to implement randomisation :)
print(len(space))
print(inv[4])
inv.append("bandage")
inv.extend(space)
# some miscellaneous array functions
