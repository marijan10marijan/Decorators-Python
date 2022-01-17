## Decorators 

def outer(function):
    def wrapper(*args, **kwargs):
        print('I am wrapper function! ')
        function(*args, **kwargs)
    return wrapper

@outer
def my_func(x,y):
    print(x + y)

x = 8
y = 11
my_func(x,y)