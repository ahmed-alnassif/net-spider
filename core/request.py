#coding=utf-8
r"""
This project created by Ahmed Al-Nassif hoping to help you learn and understand how mega sites work and the way they write code, I don't take responsibility for doing illegal things like: stealing website ownership or tricking people into stealing their information... I designed this project to save you time and effort for learning and development, and you have the right to modify it to suit your needs
Github: https://github.com/ahmed-alnassif
E-mail: Mr.Ahmed.Nassif@gmail.com
Facebook: https://fb.me/100049582051187
"""

from core.stop import check
check(__name__)

from core.User_Agent import User_Agent
from core.console import console
import json

class ErrRequest(Exception):
	pass

class Request(__import__("requests").Session):
	def user_agent(self):
		return User_Agent().user_agent
	
	def get(self, url, **kwargs):
		user_agent=self.user_agent()
		h=["headers",
		"User-Agent"]
		if kwargs.get(h[0]):
			kwargs[h[0]].update({h[1]: user_agent})
		else:
			kwargs.update({h[0]: {h[1]: user_agent}})
		try:
			return super().get(url, **kwargs)
		except Exception as e:
			raise ErrRequest(e)
	
	def post(self, url, **kwargs):
		user_agent=self.user_agent()
		h="headers"
		u="User-Agent"
		if kwargs.get(h):
			kwargs[h].update({u: user_agent})
		else:
			kwargs.update({h: {u: user_agent}})
		try:
			return super().post(url, **kwargs)
		except Exception as e:
			raise ErrRequest(e)

def Request_settings(args):
	with Request() as Request_:
		#settings requests
		try:
			Request_.headers.update(json.loads(args.header))
			Request_.cookies.update(json.loads(args.cookie))
			Request_.proxies.update(json.loads(args.proxy))
		except Exception:
			console.Error('Syntax {"key": "value"}')
			raise
			exit(0)
		else:
			return Request_
