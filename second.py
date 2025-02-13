# print("Hello World")

# i= 1
# while i<=6:
#     print(i)
#     i+=1



# def ssp (rows):
#     for i in range(rows):
#         print("* " * (i+1))

# ssp(5)



# numbers = ["first", "second", "third", "fourth", "fifth"]
# i=0
# while i<=4:
#     print(numbers[i])
#     i+=1
    

# string = "Abdullah"
# # print("" in string)
# print(len(string))


# name = input("Your Name: ")
# print(int(name))


print("Give Two Numbers")
one = int(input("Input Number One: "))
two = int(input("Input Number Two: "))
operator = input("Enter Operator: ")

if(operator=="+"):
    ans = one+two
if(operator=="-"):
    ans = one-two
if(operator=="*"):
    ans = one*two
if(operator=="/"):
    ans = one/two

print(ans)

