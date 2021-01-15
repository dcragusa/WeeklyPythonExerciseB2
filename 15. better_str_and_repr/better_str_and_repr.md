Something that has always bothered me in Python is the default output from the `__repr__` and `__str__` methods. Is 
there anyone who believes that if I define a class in the following way:

    class Bar(object):
        pass

That the most reasonable output from:

    b = Bar()
    b

Will be:

    <__main__.Bar at 0x1043991d0>

No, I didn't think so.  This is pretty useless; I don't need to know the address of the object in memory, and I 
certainly would like to know a bit more than the class. For example, I'm generally curious to see the object's 
attributes.

This week, we're going to create a decorator `betterrepr` that, when applied to a class, lets us have an alternative 
output to the defaults.  For example:

    @betterrepr()
    class Foo(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    f = Foo(10, [1,2,3,4,5])
    print(f)

I want my `betterrepr` decorator to modify `__repr__` such that the output from the above code will be:

    Instance of Foo, vars = {'x': 10, 'y': [1, 2, 3, 4, 5]}

The `betterrepr` decorator will take two optional arguments, called `newstr` and `newrepr`. It is expected that the 
passed values will be functions that will replace the default `__repr__` and `__str__` methods. If `newstr` isn't 
defined, then nothing special will happen. But if `newrepr` isn't passed, then we'll use the same default value as 
last time, overriding object's `__repr__`.
