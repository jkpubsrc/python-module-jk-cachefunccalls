

import typing
import inspect
import time
import typing




# the cache stores all data for some time
__CACHE = {}


# this is the annotation wrapper that receives arguments and returns the function that does the wrapping
def cacheCalls(seconds:int = 0, dependArgs:typing.Union[typing.List,typing.Tuple] = None):
	assert isinstance(seconds, int)
	assert seconds > 0
	if dependArgs is not None:
		assert isinstance(dependArgs, (tuple, list))
		for a in dependArgs:
			assert isinstance(a, int)
			assert a >= 0
	else:
		dependArgs = ()

	# this function is executed for every function definition
	def _wrap_the_function(fn):
		__CACHE[id(fn)] = [None, 0, None]		# lastArgID, lastT, lastResult

		argNames = inspect.getargspec(fn).args
		bIsMethod = argNames and (argNames[0] == "self")
		_nShift = 1 if bIsMethod else 0
		#print("method" if bIsMethod else "function")
		nIdentifierArgs = [ x + _nShift for x in dependArgs ]

		# this function is executed every time the wrapped function is invoked.
		def wrapped(*args, **kwargs):
			cacheRecord = __CACHE[id(fn)]

			tNow = time.time()
			extraIdentifier = ""
			for i in nIdentifierArgs:
				extraIdentifier += "|" + str(id(args[i]))

			bNeedsInvoke = False
			if "_ignoreCache" in kwargs:
				bInvalidate = kwargs["_ignoreCache"]
				assert isinstance(bInvalidate, bool)
				del kwargs["_ignoreCache"]
				bNeedsInvoke = bInvalidate

			if cacheRecord[1] <= 0:
				bNeedsInvoke = True
			elif tNow > cacheRecord[1] + seconds:
				bNeedsInvoke = True
			elif extraIdentifier != cacheRecord[0]:
				bNeedsInvoke = True

			if bNeedsInvoke:
				cacheRecord[0] = extraIdentifier
				cacheRecord[1] = tNow
				cacheRecord[2] = fn(*args, **kwargs)

			return cacheRecord[1]
		#

		return wrapped
	#

	return _wrap_the_function
#





