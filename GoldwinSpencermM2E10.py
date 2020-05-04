#Spencer Goldwin
#Delcare Constants
cupSugar = 1.5
cupButter = 1
cupFlour = 2.75
cookies = 48

#Get number of cookies
numCookies = int(input('Enter the number of desired cookies'))
cookieAmt = numCookies / cookies
#Calculate ingredient amounts
amtSugar = cupSugar * cookieAmt
amtButter = cupButter * cookieAmt
amtFlour = cupFlour * cookieAmt

#Display ingredient amounts
print('You will need the following:')
print(amtSugar, 'cups of sugar')
print(amtButter, 'cups of butter')
print(amtFlour, 'cups of flour')

