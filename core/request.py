#coding=utf-8
r"""
This project created by Ahmed Al-Nassif hoping to help you learn and understand how mega sites work and the way they write code, I don't take responsibility for doing illegal things like: stealing website ownership or tricking people into stealing their information... I designed this project to save you time and effort for learning and development, and you have the right to modify it to suit your needs
Github: https://github.com/ahmed-alnassif
E-mail: Mr.Ahmed.Nassif@gmail.com
Facebook: https://fb.me/ahm3d.nassif
"""

from core.stop import check
check(__name__)

from fake_useragent import UserAgent
from core.console import console
import json

chrome_version = "126.0.0.0"

class ErrRequest(Exception):
	pass

class Request(__import__("requests").Session):
	
	new_agent = False
	random_agent = False
	mobile = False
	
	def user_agent(self):
		ua=UserAgent(browsers=["chrome", "firefox"], platforms="mobile" if self.mobile else "pc")
		return ua.random if self.random_agent else f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36"
	
	def get(self, url, **kwargs):
		user_agent=self.user_agent()
		h=["headers",
		"User-Agent"]
		if not self.new_agent:
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
		if not self.new_agent:
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
			headers={
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
				"Accept-Language": "en-US,en;q=0.5",
				"DNT": "1",
				"Upgrade-Insecure-Requests": "1",
				"Connection": "keep-alive",
				"Sec-Fetch-Dest": "document",
				"Sec-Fetch-Mode": "navigate",
				"Sec-Fetch-Site": "none",
				"Sec-Fetch-User": "?1",
				"sec-ch-ua-platform": '"Android"',
				"sec-ch-ua": f'"Google Chrome";v="{chrome_version}", "Chromium";v="{chrome_version}", "Not=A?Brand";v="24"',
				"sec-ch-ua-mobile": "?1",
				"TE": "trailers"
			}
			headers.update(json.loads(args.header))
			if headers.get("User-Agent"):
				Request_.new_agent=True
			Request_.random_agent = args.mob if args.mob else args.random_agent
			Request_.mobile = args.mob
			Request_.headers.update(headers)
			Request_.cookies.update(json.loads(args.cookie))
			Request_.proxies.update(json.loads(args.proxy))
		except Exception:
			console.Error('Syntax {"key": "value"}')
			raise
			exit(0)
		else:
			return Request_
