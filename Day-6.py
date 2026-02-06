#29. count no of character present in your name
# name=input("Enter your nice name ")
# c=0
# for i in name:
#     c=c+1
# print("count=",c)
#30.count & print the all vowels present in your name

# name=input("Enter your nice name ").lower()
# v="aeiou"
# c=0
# for i in name:
#     if i in v:
#         print(i,end=" ")
#         c=c+1 
# print("vc=",c)

#31.find the Fibonacci series.
# n=int(input("Enter the numebr "))
# a=-1
# b=1
# # print(a,b)
# for i in range(n):
#     c=a+b
#     print(c)
#     a=b
#     b=c

#32. Write a program to Simple authentication system (login successful / failed).
# userid="raj@"
# pwd="123"
# ui=input("Enter the user id ")
# p=input("Enter the user pwd ")
# if userid==ui and pwd==p:
#     print("Login ")
# else:
#     print("Login fail")
#33.print index value and character present in given string
# name=input("Enter your nice name ").lower()
# index=0
# for i in name:
#     print(f"{index}: {i}")
#     index=index+1

#34.write a program to display the alternat even number.

# n=int(input("Enter the number "))
# for i in range(2, n+1,4):
#     print(i,end=" ")

#35.write a program to display the alternat even number is divisible by 4.
n=int(input("Enter the number "))
for i in range(2,n+1,2):
    # print(i,end=" ")
    if i%4==0:
        print(i,end=" ")


 