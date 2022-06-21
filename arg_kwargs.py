# *args
def sum(*numbers):
    result = 0
    print(numbers)
    for x in numbers:
        result += x
    return result

print(sum(5,5,10))

# **kwargs
def concat(**words):
    print(words)
    result = ''

    for x in words.values():
        result += x
    return result

print(concat(a='mukit',b='hasan',c='pranto'))

#uses of unpack op
list1 = [1,2,3]
list2 = [4,5,6]
print(sum(*list1,*list2))

list3 = [*list1,*list2]
print(list3)

dict1 = {
    'name': 'Mukit',
    'Id': '180224'
}

dict2 = {
    'dis': 'CSE'
}

dict3 = {**dict1,**dict2}

print(dict3)
