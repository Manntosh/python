def temp(c):
    f = (c * 9 / 5 + 32)
    return f

user_input = input("Enter the value in celsius: ")
change = temp(float(user_input))
print(change)

def temperature(f):
    c = (f - 32) * 5 / 9
    return c

user_input1 = input("Enter the value in faranhite: ")
change = temperature(float(user_input1))
print(change)
