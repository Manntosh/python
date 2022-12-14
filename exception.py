# try:
#     number = int(input("Enter an integer: "))
# except ValueError:
#     print("That was not an integer")



# def divide(num1,num2):
#     try:
#         print(num1/num2)
#     except (TypeError):
#         print("encountered a problem")
#     except(ZeroDivisionError):
#         print("num2 must be not zero")
    

# user_input = int(input("enter a no.:"))
# user_input1 = int(input("enter a no.:"))
# divide(user_input,user_input1)

# def divide(num1,num2):
#     try:
#         print(num1/num2)
#     except ZeroDivisionError:
#         print("don't use zero in num2")
# divide(6,0)

# while True:
#     try:
#         user_input = int(input("enter an integer: "))
#         print(user_input)
#         break
#     except ValueError:
#         print("Try Again")


try:
    user_input_num = int(input("Enter a number: "))
    user_input_str = input("enter a string: " )
    print(user_input_str[user_input_num])
except(ValueError):
    print("Enter an integer")
except(IndexError):
    print("Index is out of bound")



