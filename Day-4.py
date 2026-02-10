#16. Write a program to print the number that is divisible by 5 or 7
# for i in range(1, 101):
#     if i%5==0 or i%7==0:
#         print(i,end=" ")
#17.  multiplication table of given number
# n=int(input("jiska table aapko yad nhi no likho"))
# for i in range(1,11):
#     print(f"{n}X{i}={n*i}")

#18.Write a program to find the factorial of given number 
# n=int(input("Enter the number "))
# f=1
# for i in range(1,n+1):
#     f=f*i 
# print("factorial=",f)

#19.
# n=int(input("Enter the number "))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")

#20.
s=0
c=0
p=1
n=int(input("Enter the number "))
for i in range(1,n+1):
    if n%i==0:
        s=s+i
        c=c+1
        p=p*i
        print(i,end=" ")
print("sum=",s)
print("count=",c)
print("p=",p)