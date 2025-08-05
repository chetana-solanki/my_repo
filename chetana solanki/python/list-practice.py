# basic questions
#creat five fruits and print second
# l1= ["apple","banana","orange","lichi","papaya"]
# print(l1[1])

# # add mango to the end of the list
# l1.append("mango")
# print(l1)

# # insert apple at 2nd index
# l1.insert(2,"apple")
# print(l1)


# # remove banana from a list
# l1.remove("banana")
# print(l1)


# # find langth of a list
# print(len(l1))


# #reverse the elements
# l1.reverse()
# print(l1)

# if l1.count("orange") > 0:
#     print("orange is present")
# else:
#     print("orange is not present")

# # count how many time apple occure 
# print(l1.count("apple"))


# # sort a list ascending  and descending order
# l1.sort()
# print(l1)

# l1.sort(reverse=True)
# print(l1)



# #make a copy of a list
# m=l1.copy()
# print(m)



# intermediate level
# merge two list
# l=[1,2,3]
# m=[4,5,6]
# l.extend(m)
# print(l)


# # find the maximum and minimum number 

# l=[2,3,8,7,4,5,6]
# min_value=min(l)
# max_value=max(l)
# print(min_value)
# print(max_value)

# #remove all duplicate from list
# # method 1
# l=[2,4,6,7,8,4,5,6,4,3,2]
# unique=list(set(l))
# print(unique)

# method 2
# l=[2,4,2,6,7,8,4,5,6,4,3,2]
# unique=[]
# for i in l:
#     if i not in unique:
#         unique.append(i)
# print(unique)




#sum of all numbers in list
# l=[2,4,6,7,8,4,5,6,4,3,2]
# print(sum(l))
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)


#split a list into two lists:even and odd
# l=[2,4,6,7,8,4,5,6,4,3,2]
# even=[]
# odd=[]
# for i in l:
#      if i % 2==0:
#        even.append(i)   
#      else:
#         odd.append(i)
# print(even)
# print(odd)

# left rotation by 2
# [1,2,3,4,5] --> [2,3,4,5,1] --> [3,4,5,1,2]
# l1 = [1,2,3,4,5]
# first = l1[0]
# for i in range(0, len(l1)-1):
#     l1[i] = l1[i+1]
# l1[-1] = first
# print(l1)

#print only strings from a list containing mixed datatypes
# l1 = [1,2,True, False, [1,3,5], "anc", ["abc", "def"], None, {"def"}, (1,4,5), 3.14]
# for i in l1:
#     if isinstance(i, str):
#         print(i)



#advance level
#remove all even number fron the list
# l =[2,3,5,6,4,7,8,9,2,4]




#take a user input and print it in reverse order

# l = list(input("Enter a list :"))
# l.reverse()
# print(l)



#find common element between two lists
# l1=[2,4,5,6,7,3,4,5]
# l2=[7,5,4,3,5,7,2,6]






# my_list = [1, 2, 3, 2, 4, 5, 1]
# duplicates = set()

# for i in my_list:
#     if my_list.count(i) > 1:
#         duplicates.add(i)

# print(duplicates)