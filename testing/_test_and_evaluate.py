

import collections
import typing
import inspect
import time

import jk_cachefunccalls






def _testStd(someCallable) -> list:

	print("Testing 20 calls spanning over 10 seconds ... please wait ...")
	print()

	results = []
	for i in range(0, 20):
		#key = "abc" + str(i)
		key = inspect
		#print(">", id(key), key)

		ret = someCallable(key)
		print("\t" + str(ret))
		results.append(ret)

		time.sleep(0.5)

	# ----

	print()
	return results
#




def _testInv(someCallable) -> list:

	print("Testing ... please wait ...")
	print()

	results = []
	for i in range(0, 20):
		#key = "abc" + str(i)
		key = inspect
		#print(">", id(key), key)

		ret = someCallable(key, _ignoreCache=True)
		print("\t" + str(ret))
		results.append(ret)

		time.sleep(0.5)

	# ----

	print()
	return results
#




def _evaluateStd(results:list):

	print("Evaluating: There should be sets of four or five sets of values that are identical ...")

	c = collections.Counter()
	for n in results:
		c[str(n)] += 1
	nFound = 0
	for k, v in c.items():
		if v == 4:
			# success
			nFound += 1
	print("Found: " + str(nFound))

	if nFound < 3:
		print("ERROR!")
	else:
		print("SUCCESS!")
#





def _evaluateInv(results:list):

	print("Evaluating: There should be no sets of values that are identical ...")

	c = collections.Counter()
	for n in results:
		c[str(n)] += 1
	nFound = 0
	for k, v in c.items():
		if v > 1:
			# error
			nFound += 1
	print("Found: " + str(nFound))

	if nFound > 0:
		print("ERROR!")
	else:
		print("SUCCESS!")
#





def testAndEvaluate(someCallable, invalid:bool = False):
	assert callable(someCallable)
	assert isinstance(invalid, bool)

	if invalid:
		results = _testInv(someCallable)
		_evaluateInv(results)
	else:
		results = _testStd(someCallable)
		_evaluateStd(results)
#





