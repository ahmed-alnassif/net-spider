#coding=utf-8
r"""
This project created by Ahmed Al-Nassif hoping to help you learn and understand how mega sites work and the way they write code, I don't take responsibility for doing illegal things like: stealing website ownership or tricking people into stealing their information... I designed this project to save you time and effort for learning and development, and you have the right to modify it to suit your needs
Github: https://github.com/ahmed-alnassif
E-mail: Mr.Ahmed.Nassif@gmail.com
Facebook: https://fb.me/100049582051187
"""

from core.stop import check
check(__name__)

from core.console import console
from json import dumps, loads
import time, hashlib
__all__ = ["NetSpider_Update"]
class args(object):
	
	def __init__(self):
		self.header=dict()
		self.cookie=dict()
		self.proxy=dict()
		# Setting
		
		self.header=dumps(self.header)
		self.cookie=dumps(self.cookie)
		self.proxy=dumps(self.proxy)
		self.status="Cool"
	
	def __str__(self):
		return self.status
	
	def __repr__(self):
		return self.status

from core.request import (
User_Agent,
Request_settings,
ErrRequest,
)

Request=Request_settings(args())

class NetSpider_Update(args):
	
	def folder_name(self):
		key=str(time.time()).encode()
		x=hashlib.md5()
		x.update(key)
		return x.hexdigest()
	
	def git_clone(self):
		os=self.os
		github=self.github
		folder=self.folder
		cmd=os.popen
		if not cmd("which git").read().strip():
			console.Log("Install git")
			os.system("apt update")
			os.system("apt install -y git")
		console.Log("Installing")
		if not os.path.exists(folder):
			os.mkdir(folder)
		os.chdir(folder)
		os.system(f"git clone {github}")
		x=github.split('/')[-1]
		path=os.path.join(folder, x)
		if not os.path.exists(x):
			cmd(f"rm -f -r {folder}").readline()
			return False
		if not len(os.listdir(x)) > 0:
			cmd(f"rm -f -r {folder}").readline()
			return False
		os.chdir('..')
		cmd(f"mv -f {path}/* .").readline()
		cmd(f"rm -f -r {folder}").readline()
		return True
	
	def check(self):
		version=self.version
		url=self.url
		try:
			r=Request.get(url)
		except ErrRequest as e:
			console.Error(e)
			console.Log("Checking from your connection")
			if input("If you want continue without check from version enter y for yes or n for no: ").upper() in ['Y', 'YES']:
				return True
			else:
				return False
		else:
			x=r.text.strip()
			if x==version:
				console.Log("You are using the latest version")
				return False
			else:
				return True
	
	def setup(self):
		msg="No module"
		os=self.os
		cmd=os.popen
		console.Log("Note: if tool not working try command ` pip install -r requirements.txt ` or ` python setup.py install `")
		if msg in cmd("python -m pip").read():
			console.Error("Not found pip")
			if cmd("which easy_install"):
				console.Info("Install pip")
				os.system("easy_install pip")
			else:
				console.Info("use setup.py for install")
				os.system("python setup.py install")
		else:
			console.Log("Update pip")
			os.system("python -m pip install --upgrade pip")
			console.Info("install pakages use pip")
			os.system("python -m pip install -r requirements.txt")
		return True
	
	def __init__(self):
		console.Banner()
		console.Log("Please wait...")
		self.folder=self.folder_name()
		self.os=__import__("os")
		self.version=console.Version()
		with open("core/etc/git.json") as r:
			json=loads(r.read())
			self.github=json["github"]
			self.url=json["version"]
		reslut=self.check()
		if not reslut:
			exit(0)
		reslut=self.git_clone()
		if not reslut:
			console.Error("Failed installation")
			exit(0)
		self.setup()
	
	def __str__(self):
		return super().__str__()

#---End---#
