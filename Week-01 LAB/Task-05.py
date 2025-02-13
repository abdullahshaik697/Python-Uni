seconds= int(input("Enter time in seconds: "))
hours= seconds//3600
minutes=(seconds % 3600) / 60
remainingseconds= seconds % 60
print("time in hours,minutes and seconds:",hours," hours",minutes," minutes",remainingseconds," seconds")