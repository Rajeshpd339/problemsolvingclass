#Write a program to Check whether a given year is a leap year or not.
# year=int(input("Enter the year "))
# if year%4==0 or year%400==0 and year%100!=0:
#     print("Leap year ")
# else:
#     print("not leap year ")
#Write a program to Check the given digit is present in given number or not n=125464.
# n=125464
# n2=str(n)
# un=input("Enter your number ")
# if un in n2:
#     print("aapka number mil gya")
# else:
#     print("phir check kre ")

#3.Write a program to Check whether a given character is lowercase, uppercase, digit, or other.
# ch=input("Enter the character ") 
# if ch>='A' and ch<="Z":
#     print("upper case ")
# elif ch>="a" and ch<="z":
#     print("lower case ")
# elif ch>='0' and ch<='9':
#     print("dogit")
# else:
#     print("others ")
#4.Write a program to Sort Three Numbers in Descending Order.

# a=int(input("Enter the value of a "))
# b=int(input("Enter the value of b "))
# c=int(input("Enter the value of c "))
# if a>b and a>c:
#     if b>c:
#         print(a,b,c)
#     else:
#         print(a,c,b)
# elif b>a and b>c:
#     if a>c:
#         print(b,a,c)
#     else:
#         print(b,c,a)
# else:
#     if a>b:
#         print(c,a,b)
#     else:
#         print(c,b,a)
#5.Write a program to Check the given character are present in string or not
s="jobs jaruri shadi ke liye"
a=input("enter the character or word ").lower()
if a in s:
    print("exit")
else:
    print("not")