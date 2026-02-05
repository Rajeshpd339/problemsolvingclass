 #find the sum, Count & product of a given digit Example= 46425
# n=46425
# s=0
# c=0
# p=1
# while n>0:
#     lastno=n%10
#     s=s+lastno
#     c=c+1
#     p=p*lastno
#     n=n//10 
# print("sum=",s)
# print("count=",c)
# print("product=",p)

#22.last digiti is even or odd Example=545785
# n=5457858
# lastno=n%10
# if lastno%2==0:
#     print("last number is even")
# else:
#     print("last no is odd ")

# import math 
# n=int(input("Enter the number "))
# root=int(math.sqrt(n))
# if root*root==n:
#     print("perfect square ")
# else:
#     print("not  perfect square ")

#27.Write a program to Reverse the number
# n=int(input("Enter the number "))
# t=n
# rev=0 
# while n>0:
#     lastno=n%10
    # rev=rev*10 +lastno 
    # n=n//10
# print(t)
# print(rev)
# #palindrome  
# if t==rev:
#     print("palindrome yes ")
# else:
#     print("not")
#28 Write a program to Reverse the string 
# n="janpran"
# print(n)
# print(n[::-1])
# s=input("Enter string ")
# rev=""
# for ch in s:
#     rev=ch+rev
# print(s)
# print(rev)
# #palindrome string 
# if rev==s:
#     print("palindrome ") 
# else:
#     print("not")
