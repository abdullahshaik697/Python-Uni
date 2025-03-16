responses = ["Yes", "No", "Yes", "Maybe", "No", "Yes", "No", "No", "Maybe"]

yesCount = 0
noCount = 0
maybeCount = 0

for i in responses:
    if i == "Yes":
        yesCount+=1
    elif i == "No":
        noCount+=1
    elif i == "Maybe":
        maybeCount+=1

print(responses)
print("Total Yes in Responses", yesCount)
print("Total No in Responses", noCount)
print("Total Maybe in Responses", maybeCount)
