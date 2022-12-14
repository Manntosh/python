""" Write a script called exponent.py that receives two numbers from the user and displays the first number raised to the power of the second
number. """

base = input("enter the base: ")
exponent = input("enter the exponent: ")
final_value = int(base) ** int(exponent)
print(f"{base} to the power of {exponent} = ", final_value)

base = input("enter the base: ")
exponent = input("enter the exponent: ")
final_value = pow(int(base),int(exponent))
print(f"{base} to the power of {exponent} = ", final_value)