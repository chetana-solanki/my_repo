
# # list
# a=[2,5,3,7,6,8]
# print(a)
# print(type(a))
# print(len(a))


# # list indexing
# print(a[0:3])
# print(a[:5])
# print(a[2:])
# print(a[-5:-2])


# # list methods
# # append
# a=[1,3,5,6,7]
# a.append(2)
# print(a)


# # insert
# a=[2,3,4,5,6]
# a.insert(2,55)
# print(a)


# # extend
# a=[1,2,3,4]
# b=[3,4,5,6]
# a.extend(b)
# print(a)


# #remove
# a=[4,5,6,3,4,2]
# a.remove(5)
# print(a)


# #pop
# a=[3,4,5,2,3,4]
# a.pop(2)
# print(a)

# a.pop()   #if index is not giving then last letter remove
# print(a)


# # clear
# a=[2,3,4,5,6,3,4]
# a.clear()
# print(a)


# # del
# a=[2,4,5,3,4,5]
# del a[1]
# print(a)

# # del a
# # print(a)

# # sort
# a=[2,7,6,5,4,8,6]
# a.sort()
# print(a)         #assending


# a.sort(reverse=True)   #decending
# print(a)


# # reverse
# a=[1,2,3,6,7,4,5]
# a.reverse()
# print(a)


# # index
# a=[2,4,5,2,3,4,5,6]
# print(a.index(5))


# # count
# a=[4,3,5,6,7,4]
# print(a.count(4))


# # copy
# a=[1,2,3,4]
# b=a.copy()
# print(b)




# tuple

# a=(1,3,4,5,3,6)
# print(a)
# print(type(a))
# print(len(a))

# b=list(a)
# print(b)
# print(type(b))


# b.append(7)
# print(b)

# b.insert(2,44)
# print(b)


# c=[2,3,4]
# b.extend(c)
# print(b)

b.remove(3)
print(b)

b.pop(2)
print(b)

b.sort()
print(b)


b.sort(reverse=True)
print(b)


# b.clear()
# print(b)

a=tuple(b)
print(a)


# Index
print(a.index(7))

#count
print(a.count(5))


# sort method not working in tuple
t=(2,3,4,5,3,4,3)
# t.sort()
# print(t)


#extend method not working in tuple
# m=(1,3,4)
# t.extend(m)
# print(t)



# t1=list(t)
# t1[1]="chetana"
# print(t1)