originalPrice = int(input("Enter Original Price: "))
discountPercentage = int(input("Enter discount %: "))
discountedPrice = int((originalPrice*discountPercentage)/100)
finalPrice = originalPrice-discountedPrice

print("Final Price is: ", finalPrice)