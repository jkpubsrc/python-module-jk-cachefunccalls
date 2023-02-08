#!/usr/bin/python3


import collections
import typing
import inspect
import time

from jk_cachefunccalls import cacheCalls

from _test_and_evaluate import testAndEvaluate






@cacheCalls(seconds=2, dependArgs=[0])
def returnSomething(n):
	return time.time()
#






testAndEvaluate(returnSomething, invalid=True)





