﻿jk_cachefunccalls
==========

Introduction
------------

This python module provides an annotation that caches results of function calls automatically.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk_cachefunccalls)
* [pypi.python.org](https://pypi.python.org/pypi/jk_cachefunccalls)

Why this module?
----------------

Sometimes functions or methods provide data that are a little bit expensive to calculate. For example analysing some directory and providing information about the disk space used might take a few tens of seconds or even a few seconds. If various other components of a software want to use this information these software components might invoke a single method that performs all necessary operations and afterwards provides a single result. This module now provides an annotation that can automatically cache this result. If multiple calls to such a function or method are performed, the first call then will calculate the actual value, but successive calls might just return the last value calculated.

Of course such caching mechanism will not be feasible in every situation. But the situation just discribed where a directory must be scanned is an excellent example where such caching is useful: For the duration of a few seconds it is typically no problem to return the value just calculated a few seconds ago.

The annotation provided by this module enables you to implement such caching without any specific need for implementing such caching yourself. It is a convenient way of adding this functionality to an existing function or method without a complicated set of codelines.

How to use this module
----------------------

### Import this module

Please include this module into your application using the following code:

```python
from jk_cachefunccalls import *
```

### Annotate a function

Now after having imported the annotation named `cacheCalls` we can make use of it. Example:

```python
@cacheCalls(seconds=5)
def someFunction():
	....
	# do something complicated
	....
	return ....
```

In the example above the function `someFunction` is annotated in such a way that return values are cached for 5 seconds.

### Annotate a method

With annotating methods it is exactly the same:

```python
class MyClass(object):

	...

	@cacheCalls(seconds=5)
	def someMethod(self):
		....
		# do something complicated
		....
		return ....

	...
```

### Caching depending on an argument

Sometimes you need to depend function or method calls on argument(s). If arguments exists, the caching mechanism can take them into consideration. For that you can specify an additional annotation parameter that defines the *index* of the argument(s) to consider. Example:

```python
@cacheCalls(seconds=5, dependArgs=[0])
def someFunction(hostName:str):
	....
	# do something complicated
	....
	return ....
```

Here we depend all caching on the very first argument. If this is a host name and successive calls to this function are performed specifying always the same host name, caching will provide the last value calculated (within a window of 5 seconds). However if a call is performed with a **different** host name, the cache value will be **discared immediately**. If multiple calls are performed specifying this new, different host name, the cached value will be returned again.

In summary:
* If you invoke such a function specifying a different value on every call, the function is always executed as there would be no caching.
* If you invoke such a function specifying the same value as you did in the last call, the anntation wrapper will return a cached value (if available).

Please note that this kind of caching is based on the id of an argument value (derived by `id()`). If you specify constants (such as integers or strings) python ensures that those values have the same id. **This implies if you specify an object of some kind as an argument the caching mechanism is not based on the value(s) stored in such an object but by on the identify of such an object.**

The reason for this is simple: E.g. if you would like to depend some function call on an object representing a network connection to a specific host or service, there likely will be a new object for every single connection as typically such connection objects are not reused but created again if a new connection is required. Using `id()` is very fast so caching will not depend on more complex calculations but simply on the identity of such an argument object. However if you modify the state of such an object this is not recognized: **The value cached previously might be returned.**

In this implementation we give speed of caching a greater emphasis than the exact state of an argument object. It is your responsibility as a programmer to know about the consequences of such caching (and the implications using the ids of arguments) in order to have your program behave correctly.

### Ignoring the cache

Sometimes it is required to ignore a value that might have been cached. For this use the `_ignoreCache` argument if you invoke such an annotated function:

```python
x = someFunction("localhost", _ignoreCache=True)
```

If you specify `_ignoreCache` this will control the behaviour of the wrapper around the function to be invoked. If you specify `True` here the wrapper will ignore the cache (but will cache the new value returned by the invoked function).


Contact information
-------------------

This work is Open Source. This enables you to use this work for free.

Please have in mind this also enables you to contribute. We, the subspecies of software developers, can create great things. But the more collaborate, the more fantastic these things can become. Therefore Feel free to contact the author(s) listed below, either for giving feedback, providing comments, hints, indicate possible collaborations, ideas, improvements. Or maybe for "only" reporting some bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



