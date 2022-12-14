user_input = input("enter the number: ")
user_input1 = round(float(user_input),2)
print(f"{user_input} rounded to 2 decimal places is ", user_input1)

##Write a script that asks the user to input a number and then displays the absolute value of that number. When run, your program
##should look like this:

user_in_abs = input("enter your number: ")
user_in_abs_final = abs(float(user_in_abs))
print(f"{user_in_abs} the absolute value is ", user_in_abs_final)

user_in1 = input("enter your 1st number: ")
user_in2 = input("enter your 2nd number: ")
final_out = float(user_in1) - float(user_in2)
print(f"The difference between {user_in1} and {user_in2} is an integer?",final_out,final_out.is_integer())