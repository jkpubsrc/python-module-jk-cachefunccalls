#!/usr/bin/python3


import collections
import typing
import inspect
import time

from jk_cachefunccalls import cacheCalls, clearCache

from _test_and_evaluate import testAndEvaluate




class MyTestClass(object):

	@cacheCalls(seconds=2, dependArgs=[0])
	def returnSomething(self, n):
		ret = time.time()
		clearCache()
		return ret
	#

#



o = MyTestClass()

testAndEvaluate(o.returnSomething, invalid=True)





