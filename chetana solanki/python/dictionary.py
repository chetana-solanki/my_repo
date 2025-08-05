# dictionary
# collection of key-value pairs
# mutable

dic = {
    "name":"chetana",
    "age": 25,
    "city": "indore"
}
print(dic["name"],dic["age"],dic["city"])

#update
a={122:22,123:45,124:33}
b={125:22,126:22}
a.update(b)
print(a)


# clear
# a.clear()
# print(a)

# pop
a.pop(122)         #pop items which key is given
print(a)


#popitem
a.popitem()     #popitems last items
print(a)


#del
del a
print(a)



