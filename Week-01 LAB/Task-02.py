principleAmount = float(input("Enter Principle Amount: "))
interestRate = float(input("Enter Annual Interest Rate: "))
time = float(input("Enter Time Period(in years): "))

simpleInterest = (principleAmount*interestRate*time)/100

print("Total Interest is: ",simpleInterest)