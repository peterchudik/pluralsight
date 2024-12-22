#---------------------------------------------
# __call__ -> object becomes callable
#---------------------------------------------

import socket

class Resolver:
	def __init__(self):
		self._cache = {}

	def _resolve(self, host):
		if host not in self._cache:
			self._cache[host] = socket.gethostbyname(host)
		return self._cache[host]

	def resolve(self, host):
		return self._resolve(host)

	def __call__(self, host):
		return self._resolve(host)
