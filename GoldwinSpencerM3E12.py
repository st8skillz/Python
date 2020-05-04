# Declaring variables
numPackages = int(input("How many packages are purchased? "))
RETAIL = 99

# Determine the discount
if numPackages >= 10 and numPackages< 19:
    discount = 0.1
elif numPackages >= 20 and numPackages<= 49:
    discount = 0.2
elif numPackages >= 50 and numPackages<= 99:
    discount = 0.3
elif numPackages >= 100:
    discount = 0.4
else: discount = 0

# Calculate the discount
numDiscount = (numPackages * RETAIL) * discount

# Calculate the total sale
totalSale = (numPackages * RETAIL) - numDiscount
# Display the results
print("The amount of your discount is $", format(numDiscount, '.2f'), sep='')
print("The total amount of the purchase after the discount is $", format(totalSale, ',.2f'), sep= '')

    

    
