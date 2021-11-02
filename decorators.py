
#Decorator is a function that takes another function as an argument and returns a modified version of that function.

def double_args(func):
    def wrapper(a,b):
        return func(a*2, b*2)
    return wrapper
@double_args #decorator
def multiply(a, b):
    return a * b
print(multiply(2,4))

#example 2
def double_args(func):
    def wrapper(a,b):
        return func(a*2, b*2)
    return wrapper
def multiply(a, b):
    return a * b
multiply = double_args(multiply)
print(multiply(2,4))


#example3
def print_return_type(func):
  # Define wrapper(), the decorated function
  def wrapper(*args,**kwargs):
    # Call the function being decorated
    result = func(*args,**kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def foo(value):
  return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))

#example 4
from functools import wraps
def timer():
  @wraps(func)
  def wrapper(*args,**kwargs):
    start = time.time()
    result = func(*args,**kwargs)
    timetaken = time.time() - start
    print('{} took {}s'.format(func.__name__, timetaken))
    
    return result
  return wrapper
# example 5
from functools import wraps

def add_hello(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)