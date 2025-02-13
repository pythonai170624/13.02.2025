
class A:
    def __str__(self):
        return "!A!"

def foo(fun):
    fun('hi')


def create(class_name):
    return class_name()

foo(print)
print(create(A))

