#Spencer Goldwin
#Declare constant

#Enter User data
principal = float(input('Enter Principal amount:'))
interestRate = float(input('Enter interest rate:'))
compound = int(input('Enter compound rate:'))
numYears = int(input('Enter the number of years:'))
interestRatePercent = (interestRate / 100)
#Calculate
totalAmount = principal * (1 + (interestRatePercent/compound))**(compound*numYears)

#display results

print('The total amount will be', totalAmount)
