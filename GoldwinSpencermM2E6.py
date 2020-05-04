#Spencer Goldwin
#Declare constants
stateSalesTax = 0.05
countySalesTax = 0.025
#Ask user for purchase amount
purchaseAmount = float(input('Enter purchase amount:'))
#Calculate tax
calcStateTax = stateSalesTax * purchaseAmount
calcCountyTax = countySalesTax * purchaseAmount
totalTax = calcStateTax + calcCountyTax
#Calculate Total Amount
totalAmount = purchaseAmount + totalTax
#Display the results
print('The purchase amount is', purchaseAmount)
print('The state sales tax is', calcStateTax)
print('The county tax is', calcCountyTax)
print('The total tax is', totalTax)
print('The total amount is', totalAmount)

