
class A:
    def __str__(self):
        return "!A!"

def foo(fun):
    fun('hi')


def create(class_name):
    return class_name()

foo(print)
print(create(A))

def abc(a, b, c):
    print(a, b, c)

def kwargss(**kwargs):
    print(kwargs)
    print(type(kwargs))

abc(*[1, 2, 3])
kwargss(**{'name': 'danny'})
kwargss(name='danny')

dict1 = {'x': 1, 'y': 2}
dic2 = {**dict1, 'z': 3}

def print_list(*args):
    print('args: ', args)

list1 = [1,2,3]
list2 = [*list1, 4, 5]
print(list2)
list3 = [list1, 4, 5]
print_list(*(4, 5, 6))