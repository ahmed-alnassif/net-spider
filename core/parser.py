#coding=utf-8
r"""
This project created by Ahmed Al-Nassif hoping to help you learn and understand how mega sites work and the way they write code, I don't take responsibility for doing illegal things like: stealing website ownership or tricking people into stealing their information... I designed this project to save you time and effort for learning and development, and you have the right to modify it to suit your needs
Github: https://github.com/ahmed-alnassif
E-mail: Mr.Ahmed.Nassif@gmail.com
Facebook: https://fb.me/100049582051187
"""

from core.stop import check
check(__name__)

from core.request import (
User_Agent,
Request_settings,
ErrRequest,
)

from core.console import *
#from tqdm import tqdm as List
from bs4 import BeautifulSoup as Html
from urllib.parse import urljoin, urlparse
import os, io


class ErrSpider(Exception):
	r"""
	To find out errors and show them in the program
	"""
	pass

class spider_parser(object):
	items=dict()
	#Types data fornt-end: css, javascript, images
	types={
	'link': {'if':{'rel': 'stylesheet', 'href': True}, 'get':'href', 'type': ['style', 'css']},
	'script':{'if': {'src': True}, 'get': 'src', 'type': ['javascript', 'js']},
	'img': {'if': {'src': True}, 'get': 'src', 'type': ['image', 'png']},
	}
	
	def parseurl(self):
		raw=self.raw
		types=self.types
		url=self.url
		self.links=dict()
		console.Info('Parse the page')
		soup=Html(raw, 'html.parser')
		for style in soup.find_all('style'):
			style=style.text
			self.format=types['link']['type']
			self.css(style, url)
		for key, value in types.items():
			attr=value['get']
			format=value['type']
			for tag in soup.find_all(key, **value['if']):
				link=tag[attr]
				func=link.lower().startswith
				if any([func('https://'), func('http://')]):
					if self.host:
						if urlparse(self.url).netloc==urlparse(link).netloc:
							self.links.update({link: [link, {'type': key}, format]})
						else:
							pass
					else:
						self.links.update({link: [link, {'type': key}, format]})
				elif func('//'):
					link='http://'+link[2:]
					if self.host:
						if urlparse(self.url).netloc==urlparse(link).netloc:
							self.links.update({link: [link, {'type': key}, format]})
					else:
						self.links.update({link: [link, {'type': key}, format]})
				else:
					newlink=urljoin(url, link)
					self.links.update({link: [newlink, {'type': key}, format]})
		return True
	
	def joinDict(self):
		links=self.links
		console.Info('Connect the elements :)')
		for i in links.keys():
			link=links[i][0]
			path=urlparse(link).path
			if path.startswith('/'):
				path=path[1:]
			path=path[:-1] if path.endswith('/') else path
			counter=0
			while True:
				if path in self.items.values():
					if '.' in path:
						end=path.split('.')
						end[-2]+=f"_{counter}"
						path='.'.join(end)
					else:
						path+='_'
						path+=str(counter)
					counter+=1
				else:
					counter=0
					break
			self.items.update({i: path})
	
	def nice_html(self, html):
		tag=list()
		line='\n'
		space='\t'
		begin=['</', '<']
		end=['>', '/>']
		for i in html.split(begin[0]):
			if i[:1]!=begin[0][:1]:
				i=i.split(end[0])[0]
				tag.append(begin[0]+i+end[0])
		for i in html.split(begin[1]):
			if end[1] in i:
				i=i.split(end[1])[0]
				tag.append(begin[1]+i+end[1])
		for x in tag:
			pass
	
	def css(self, data, url):
		#if not hasattr(self, "re"):
			#self.re=__import__("re")
		name=self.name
		#re=self.re
		paths=list()
		raw=list()
		link=list()
		close=";"
		Path=os.path
		if type(data)==bytes:
			data=data.decode('utf-8')
		for line in data.split(close):
			if all([True if _ in line else False for _ in ['url', '(', ')']]):
				try:
					x=line.split('url(')[1].split(')')[0]
				except IndexError:
					continue
				else:
					raw.append(x)
		for u in raw:
			if u[:6].lower() in  ["http:/", "https:"]:
				if self.host:
					if urlparse(url).netloc==urlparse(u).netloc:
						link.append(u)
				else:
					link.append(u)
			elif u[:5].lower()=="data:":
				continue
			else:
				u=urljoin(url, u)
				link.append(u)
		for u in link:
			path=urlparse(u).path
			path=path[1:] if path[:1]=='/' else path
			xpath=path
			n=0
			while True:
				if Path.exists(Path.join(name, xpath)):
					xpath=xpath.split('/')
					if '.' in xpath[-1]:
						end=xpath[-1].split('.')
						end[-2]+=f'_{n}'
						xpath[-1]=','.join(end)
					else:
						xpath[-1]+=f'_{n}'
					xpath='/'.join(xpath)
					if Path.exists(Path.join(name, xpath)):
						xpath=path
					n+=1
				else:
					path=xpath
					break
			paths.append(path)
		self.length_c+=len(link)
		for url, path in zip(link, paths):
			self.res('unknown', url, path)
		else:
			for old, new in zip(raw, paths):
				data=data.replace(old, new)
			else:
				return data
	
	def replace(self):
		sign=str()
		sign+='\n'
		sign+='<!-- '
		sign+=self.sign
		sign+=' -->'
		raw=self.raw
		items=self.items
		for k, v in items.items():
			raw=raw.replace(k, v)
		else:
			raw+=sign
			return {"name": "index.html", "data": raw}
	
	def res(self, type, url, file):
		proggress.begin(self.length_c)
		proggress.end()
		try:
			if type=='img':
				mode='wb'
				raw=Request.get(url).content
			elif type=='unknown':
				n='.cache'
				r=Request.get(url)
				if False: #url.split('.')[-1].lower() in self.image:
					mode='wb'
					raw=r.content
				else:
					try:
						mode='w'
						text=r.text
						with open(n, mode) as w:
							w.write(text)
							w.close()
						raw=r.text
					except Exception:
						try:
							content=r.content
							mode='wb'
							with open(n, mode) as w:
								w.write(content)
								w.close()
							raw=r.content
						except Exception:
							e='Type data '+type
							console.Error(e)
							raise ErrSpider(e)
			else:
				mode='w'
				raw=Request.get(url).text
			if self.format[-1]=='css':
				raw=self.css(raw, url)
			self.saveFile(raw=raw, nameFile=file, mode=mode)
		except Exception as e:
			console.Error(e)
			console.Log(f'{yllow}URL:{white} {url}')
			console.Info('for help Enter: h or help')
			while True:
				proggress.stop()
				inp=input(' '*65+'\rcontinue [T|Y|N]: ').upper()
				if inp in ['T', 'TRY']:
					proggress.num_tow-=1
					self.res(type, url, file)
					break
				elif inp in ['Y', 'YES']:
					proggress.num_tow-=1
					proggress.num_one-=1
					break
				elif inp in ['N', 'No']:
					raise
					exit(0)
				elif inp in ['H', 'Help']:
					console.Log('[1] Enter T || Try for try agent')
					console.Log('[2] Enter Y || Yes for pass')
					console.Log('[3] Enter N || No for stop in error')
				else:
					console.Error('Invalid option')
			proggress.run()
	
	def request(self):
		links=self.links
		items=self.items
		console.Info('Download files: js, css, images, fonts, ...')
		#assert len(array[0])==len(array[1])
		self.length_c+=len(links)
		for link, file in zip(links.values(), items.values()):
			url=link[0]
			type=link[1]['type']
			self.format=link[2]
			self.res(type, url, file)
	
	def saveFile(self, raw=None, nameFile=None, mode='w'):
		url=self.url
		folder="etc"
		Path=os.path
		isfile=Path.isfile(folder)
		if not Path.exists(folder) or isfile:
			if isfile:
				os.remove(folder)
			os.mkdir(folder)
		name=str()
		if hasattr(self, "name"):
			name=self.name
		else:
			count=len(os.listdir(folder))
			count=str(count)
			name+=urlparse(url).netloc if url else "object"
			name+='_'
			name+=count
			name=Path.join(folder, name)
			self.name=name
		if not Path.exists(name):
			os.makedirs(name)
		elif not Path.isdir(name):
			os.remove(name)
			os.makedirs(name)
		if not nameFile:
			return False
		if len(nameFile.split('/')) > 1:
			dir=nameFile.split('/')[:-1]
			dir="/".join(dir)
			dir=Path.join(name, dir)
			if not Path.exists(dir):
				os.makedirs(dir)
		dir=Path.join(name, nameFile)
		if self.debug:
			console.Log('Path files: '+dir)
		with io.open(dir, mode) as Write:
			Write.write(raw)
			return dir
	
	def __init__(self, debug=None, url=None, raw=None, host=None, name=None, hide_bar=None, update=None):
		r"""
		this main activity
		for repository
		
		debug:
			show some activities
			for use (e.g debug=True)
		url:
			url website for download page and get files
			(e.g url="http://www.example.com" )
		raw:
			use for put data page without download agent
			(e.g raw=open("page.html").read())
		host:
			get files only form domain selected form url
			example:
				url='http://url.com'
				get all files form http://url.com only
			use (e.g host=True)
		name:
			set new name for folder
			mean save files in folder in new name
			use (e.g name="Site")
			so all data now save in folder: Site
		"""
		start=time.time()
		self.debug=debug
		self.host=host
		self.url=url
		self.length_c=int()
		self.sign="Net-Spdir https://github.com/ahmed-alnassif/net-spider"
		self.image=['jpg', 'jpeg', 'pjpeg', 'png', 'webp', 'gif', 'io', 'xpng']
		if update:
			from core.update import  NetSpider_Update
			exit(NetSpider_Update())
		console.Banner()
		proggress.begin(1)
		if hide_bar:
			proggress.display()
		if url and not raw:
			console.Info('Download the page')
			try:
				r=Request.get(url)
			except ErrRequest as e:
				console.Error(e)
				raise
			else:
				if not (r.status_code > 199 and r.status_code < 300):
					status="request status <%s>"%r.status_code
					console.Error(status)
					raise ErrRequest(status)
				else:
					self.raw=r.text
					del r
		elif raw:
			self.raw=raw
		else:
			e="set key word args"
			console.Error(e)
			raise ErrSpider(e)
		if name:
			self.name=name
		self.parseurl()
		self.joinDict()
		replace=self.replace()
		self.saveFile(raw=replace['data'], nameFile=replace['name'])
		proggress.run()
		self.request()
		proggress.stop()
		end=round(time.time()-start, ndigits=1)
		console.Info("Program finished in: %ss ..."%end)
		console.Info(f"Files saved in: {green}{self.name}")
		console.Info(f"Count files: {cyan}{proggress.num_one}")
		console.Info("Thank you for use Net-Spider :)")
	
	def __str__(self):
		return "Target<[%s]>"%self.url

###End###
