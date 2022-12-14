# n = 1
# while n < 5:
#     print(n)
#     n = (n+1)*-5

# word = "Python"
# index = 0

# while index < len(word):
#     print(word[index])
#     index = index + 1

# for abc in "Python":
#     print(abc)

# a = "mantoshkumarsingh"
# print(a[2])
# index = 2
# while index < len(a):
#     print(a[index])
#     index = index + 4

# user_input = float(input("enter the amount: "))

# for n in range(2,6):
#     output1 = user_input/n
#     print(output1)
    


# for n in range(2,11):
#     print(n)
#     n = n+1

# n = 2
# while n <= 10:
#     print(n)
#     n = n+1


# for n in range(1, 4):
#     for j in range(4, 7):
#         print(f"n = {n} and j = {j}")


# Write a function called doubles() that takes one number as its input
# and doubles that number. Then use the doubles() function in a
# loop to double the number 2 three times, displaying each result on
# a separate line. Here is some sample output:

def doubles(a):
    final = int (a * 2)
    return final
user_input = input("insert the number: ")
for n in range(0,3):
    user_input = doubles(int(user_input))
    print(user_input)
