## Decorators using class

class DecoratorClass(object):

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print('Call method print first. ')
        return self.function(*args, **kwargs)

@DecoratorClass
def func(num1, num2):
    print(num1 * num2)

func(3,5)