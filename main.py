
# overloading

def foo(x, *args, **kwargs):
    print(args)
    print(kwargs)

foo(1, 2, 3, name='danny', age=18)
# a, b, c = [1, 2, 3]

d1 = { 'name':'danny', 'age':18 }
#     'name':'danny', 'age':18
d2 = { **d1                     , 'new_filed': 'hi' }
l3 = [1,2,3]
l4 = [*l3, 5, 6, 7]
print(d2)
print(l4)


