# QUESTION 1
score = int(input("what did you score on the test? > "))
while (score > 100) and (score < 0):
    print("that doesn't make sense!")
    score = int(input("what did you ACTUALLY score on the test? > "))
if score >= 80:
    print("your grade is A ")
elif score >= 60:
    print("your grade is B")
elif score >= 50:
    print("your grade is C")
else:
    print("ohhhh... it looks like you failed this one :( oh well theres always next time.. good luck!")
print("thanks for playing my video game! see u later")
# QUESTION 2
for n in range(0, 100, 5):
    print(n)
# QUESTION 3
cars = ["honda", "toyota", "peugeot"]
colours = ["blue", "red", "pink", "black"]
for i in cars:
    for j in colours:
        print(i, j)
# QUESTION 4
# (I)
city = []
# (II)
while len(city) < 5:
    city.append(str(input("type the name of a city! > ")))
print("hey.. nice cities, thanks :P")
# (III)
print(len(city))
# (IV)
city.append("hong")
# (V)
del city[0]
# (VI)
city.reverse()
# showing my work!
for p in city:
    print(p)
