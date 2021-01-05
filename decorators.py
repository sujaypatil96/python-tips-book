# everything in Python is an object

def hi(name="sujay"):
    return "hi " + name

print(hi())
# output: 'hi sujay'

# We can even assign a function to a variable like
greet = hi
# We are not using parentheses here because we are not calling the function hi
# instead we are just putting it into the greet variable. Let's try to run this

print(greet())
# output: 'hi sujay'

# Let's see what happens if we delete the old hi function!
del hi
print(hi())
#outputs: NameError

print(greet())
#outputs: 'hi sujay'


# defining functions within functions

def wrapper(name="sujay"):
    print("now you are inside the wrapper() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the wrapper() function")

wrapper()
#output:now you are inside the wrapper() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the wrapper() function

# This shows that whenever you call wrapper(), greet() and welcome()
# are also called. However the greet() and welcome() functions
# are not available outside the wrapper() function e.g:

greet()
#outputs: NameError: name 'greet' is not defined


# returning functions from within functions

def func_wrapper(name="sujay"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "sujay":
        return greet
    else:
        return welcome

a = func_wrapper()
print(a)
#outputs: <function greet at 0x7f2143c01500>

#This clearly shows that `a` now points to the greet() function in hi()
#Now try this

print(a())
#outputs: now you are in the greet() function


# passing a function as an argument to another function

def ret_hi():
    return "hi sujay!"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing ret_hi()")
    print(func())

doSomethingBeforeHi(ret_hi)
#outputs:I am doing some boring work before executing ret_hi()
#        hi sujay!


# creating decorators without using '@' syntax

def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction()

a_function_requiring_decoration()
#outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()


# creating decorators using '@' syntax

@a_new_decorator
def a_function_requiring_decoration2():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

a_function_requiring_decoration2()
#outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

#the @a_new_decorator is just a short way of saying:
a_function_requiring_decoration2 = a_new_decorator(a_function_requiring_decoration2)

print(a_function_requiring_decoration.__name__)
# Output: wrapTheFunction
