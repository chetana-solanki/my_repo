#print numbers from 1 to 10
# for i in range(1,11):
#     print(i)

#print the frist 10 even number
# first method:-
# for i in range(2,21,2):
#     print(i)


#second method:-
# for i in range(2,21): 
#     if i%2==0:
#        print(i)


#print The multiple table of a number:
# a=int(input("Enter a number:")) 
# for i in range(1,11):
#    print(i*a)


# print the element of list
# fruits= ["apple","banana","cherry","date"]
# for i in fruits:
#     print(i)
    

# print number from 10 to 1 reverse order ---> WRONG
# for i in range(10, 0, -1):
#      print(i,end=" ")
# print()

#     * 
#    * *
#   * * *
#  * * * *
# * * * * *


# for i in range(1,6):
#     for j in range(5-i):
#         print(" ", end="")
#     for k in range (1,i+1):
#         print("* ",end="")
#     print()





# for i in range(1,6):
#     for j in range (1,i+1):
#         print("*",end="")
#     print()




# for i in range(1,6):
#     for j in range(5-i):
#         print(" ", end="")
#     for k in range (1,i+1):
#         print("*",end="")
#     print()




# n=5
# for i in range(1,n+1):
#     print(" "* (n-i)+"*"*(2*i-1))




# 11
# n=int(input("Enter a number:"))
# for i in range(1,n):
#     if i % 13==0:
#         print("skip")
#     else:
#         print(i)






# take user input until number is less than 100
# while True:
#     num = int(input("Enter a number: "))
#     if num < 100:
#         print("Number is less than 100. Exiting loop.")
#         break
#     else:
#         print("Number is 100 or more. Try again.")
    




# print factorial of a number:-
# n=int(input("Enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)


#count how many vowels are in given string:-7
# n=input("Enter a string:")
# count=0
# for i in n:
#     if  i in 'aeiou':
#         count+=1
# print("number of vowel",count)



# print a trangle pattern:-9
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")

#     print()



#print a factorial of a number using for loop:-10
# n=int(input("Enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)


# find a maximum number in a list usig a loop:-11
l = [1,5,7,8,5,4,9,25]
max=[0]
for i in l:
    if i>max:
     print(i)    