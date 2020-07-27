#Write a program that takes a number as a user input and tells the user if it is even or odd. 

user_num = int(input("Enter a number "))

if (user_num % 2) == 0:
   print("{0} is Even".format(user_num))
else:
   print("{0} is Odd".format(user_num))