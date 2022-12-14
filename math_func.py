## Rounding function

num_round = round(3.1412123,4)
print(num_round)

#Discrepancies in rounding
num_round1 = round(3.5)
print(num_round1)

num_round2 = round(4.5)
print(num_round2)

##absolute function use to provide absolute vale i.e. positive number

num_absolute = abs(-65)
print(num_absolute)

## Power function is use to compute the power of a number

num_power = pow(2,12)
print(num_power)

## We can use the pow() function to compute the power of a number and then find the modulus with 3rd number

num_power_modulo = pow(2,12,3)
print(num_power_modulo)

## Method to check whether a value is integer or not
num_check = 3.2
print(num_check.is_integer())