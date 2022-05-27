#coding=utf-8
r"""
This project created by Ahmed Al-Nassif hoping to help you learn and understand how mega sites work and the way they write code, I don't take responsibility for doing illegal things like: stealing website ownership or tricking people into stealing their information... I designed this project to save you time and effort for learning and development, and you have the right to modify it to suit your needs
Github: https://github.com/ahmed-alnassif
E-mail: Mr.Ahmed.Nassif@gmail.com
Facebook: https://fb.me/100049582051187
"""

from core.stop import check
check(__name__)

import time
#colors
white="\033[37m"
cyan="\033[36m"
pink="\033[35m"
blue="\033[34m"
yllow="\033[33m"
green="\033[32m"
red="\033[31m"
black="\033[30m"
blod="\033[1m"
none="\033[0m"
bbb="#8700C2"
fff="\033[3J"
ddd="\033[2J"
hhh="\033[H"

class Console(object):
	
	def Println(self, text, **kwargs):
		print(text+'  ', **kwargs)
	
	def Time(self, color):
		return "\033[1;37m["+color+time.strftime("%I:%M:%S\033[37m]\033[0m")
	
	def Log(self, text, input=None, **kwargs):
		t=self.Time(blue)
		main=f"{t} {blod}{white}[{blue}LOG{white}]{none}{white} {text}{none}"
		if input:
			return main
		self.Println(main, **kwargs)
	
	def Info(self, text, input=None, **kwargs):
		t=self.Time(green)
		main=f"{t} {blod}{white}[{green}INFO{white}]{none}{white} {text}{none}"
		if input:
			return main
		self.Println(main, **kwargs)
	
	def Error(self, text, input=None, **kwargs):
		t=self.Time(red)
		main=f"{t} {blod}{white}[{red}ERROR{white}]{none}{white} {text}{none}"
		if input:
			return main
		self.Println(main, **kwargs)
	
	def Clear(self):
		self.Println(f"{hhh}{ddd}{fff}", end='')
	
	def Version(self):
		default="version: 22.5.27"
		file="core/etc/version.txt"
		try:
			data=open(file).read().strip()
			assert len(data) > 0
		except Exception:
			open(file, 'w').write(default)
			data=default
		return data.split(':')[-1].strip()
	
	def Banner(self):
		self.Clear()
		version=self.Version()
		path=self.os.path
		logo='core/etc/banner.txt'
		if not path.exists(logo):
			with open(logo, 'w') as w:
				w.write(" Net-Spider")
				w.close()
		
		with open(logo, 'r') as r:
			R=r.read()
			self.Println("{}{}Created By: {}{}Ahmed Al-Nassif{}".format(R, white, blod, green, none))
			self.Println("{}{}Github: {}https://github.com/ahmed-alnassif{}".format(blod, black, white, none))
			self.Println("{}{}E-mail: {}Mr.Ahmed.Nassif@gmail.com{}".format(blod, white, pink, none))
			self.Println("{}{}Facebook: {}https://fb.me/100049582051187{}".format(blod, blue, white, none))
			self.Println("{}{}Porgram version{}: {}{}{}".format(blod, red, white, yllow, version, none))
			print()
			del R
	
	def __init__(self):
		self.os=__import__("os")
		pass
	
	def __str__(self):
		return "Working"

class Proggress(object):
	
	state=None
	
	def stdout(self, *args, flush=True, end=str(), sep=str(),  **kwargs):
		print(*args, flush=flush, end=end, sep=sep, **kwargs)
		#self.sys.stdout.write(str().join(args))
		#self.sys.stdout.flush()
		
	
	def show(self):
		self.stdout(self.s)
	
	def hide(self):
		self.stdout(self.e)
	
	def display(self, mode=None):
		self.Display=mode
	
	def spinner(self):
		"""c=['counter_one', 'counter_tow']
		if globals().get(c[0]) is None:
			globals()[c[0]]=0
		if globals().get(c[1]) is None:
			globals()[c[1]]=0"""
		
		while self.state: #and self.num_one > self.num_tow:
			n1=self.num_one
			n2=self.num_tow
			h=100
			m='\x1b[38;2;141;0;234m'
			mm='\x1b[38;2;181;57;255m'
			x='█'
			s=" ";f="|"
			total=round((n2/n1)*h, ndigits=1)
			bar=int(total/5)
			bar_space=int(h/5)-bar
			total_str="({0}/{1})".format(n1, n2)
			total_h_str="{0}%".format(total)
			bar_str=x*bar+s*bar_space
			#print
			Time=self.console.Time(mm)
			self.stdout(Time, s, blod, white, '[', m, 'BAR', white, ']', m, ':', s, white, total_h_str, s, mm, f, bar_str, f, s, m, total_str, none, '\r')
			#time.sleep(0.4)
		else:
			self.stop()
	
	def begin(self, *args):
		if args==list():
			self.num_one=0
		else:
			self.num_one=sum(args)
	
	def end(self):
		if not hasattr(self, "num_tow"):
			self.num_tow=0
		self.num_tow+=1
	
	def init(self):
		try:
			self.spinner()
		except Exception:
			self.stop()
			raise KeyboardInterrupt
	
	def run(self):
		if not self.Display:return
		self.state=True
		self.show()
		self.thread(target=self.init).start()
	
	def stop(self):
		self.state=False
		self.hide()
		self.stdout(' '*65+'\r')
	
	def __init__(self, console):
		self.num_one=0
		self.num_tow=0
		self.s='\x1b[?25l\x1b[?7l\x1b[0m\x1b[32m\x1b[1m'
		self.e='\x1b[?25h\x1b[?7h'
		self.Display="block"
		self.thread=__import__("threading").Thread
		#self.sys=__import__("sys")
		self.console=console
	
	def __str__(self):
		return "<[working]>"

console=Console()
proggress=Proggress(console)
