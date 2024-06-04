#!/usr/bin/python
#coding=utf-8
r"""
This project created by Ahmed Al-Nassif hoping to help you learn and understand how mega sites work and the way they write code, I don't take responsibility for doing illegal things like: stealing website ownership or tricking people into stealing their information... I designed this project to save you time and effort for learning and development, and you have the right to modify it to suit your needs
Github: https://github.com/ahmed-alnassif
E-mail: Mr.Ahmed.Nassif@gmail.com
Facebook: https://fb.me/ahm3d.nassif
"""

import sys
#check
if sys.version_info.major < 3:
	print('[-] This program only works with version 3 of Python ):')
	print('python %s --help'%sys.argv[0])
	sys.exit(0)

import core
from core.console import console, proggress
console.Log('Starting porgram ...')

class Program(object):
	
	def ArgParse(self):
		arg_parse=self.argparse.ArgumentParser(formatter_class=self.argparse.RawTextHelpFormatter, usage='python %s -u [url]'%self.name, description="This project designed to retrieve the source code for a web page, including front-end elements such as JavaScript, CSS, images, and fonts.", add_help=False)
		arg_opt=arg_parse.add_argument_group("Net-Spider")
		arg_opt.add_argument("--help", dest="help", action="store_true",default=False,help="Show usage and help parameters")
		arg_opt.add_argument("-u",metavar="", dest="url", default=None, help="Target URL (e.g. http://example.com)")
		arg_opt.add_argument("-d", "--domain", dest="host", action="store_true", default=None, help="Pull links from the primary website address only")
		arg_opt.add_argument("--name", dest="name", default=None, help="The name of the folder in which to save the site files")
		arg_opt.add_argument("--hide", dest="bar", action="store_true", default=None, help="Hide the progress bar [----]")
		arg_opt.add_argument("-v", dest="view", action="store_true", default=None, help="Give more output.")
		arg_opt.add_argument("--page", dest="raw", default=None, help="Parse an HTML file and retrieve all files from it")
		arg_opt.add_argument("--update", dest="update", action="store_true", default=None, help="Automatically update the tool")
		arg_opt=arg_parse.add_argument_group("Requests settings")
		arg_opt.add_argument("--random-agent", dest="random_agent", action="store_true", default=None, help="Random user agent")
		arg_opt.add_argument("--mobile", dest="mob", action="store_true", default=None, help="make requests as mobile default: PC, Note: this option will active random agent")
		arg_opt.add_argument("--cookie",help='Set cookie (e.g {"ID": "1094200543"})',default='{}',metavar="")
		arg_opt.add_argument("--header",help='Set header (e.g {"User-Agent": "Chrome Browser"})',default='{}',metavar="")
		arg_opt.add_argument("--proxy",default='{}', help='Set proxy (e.g. {"https":"https://10.10.1.10:1080"})')
		args=arg_parse.parse_args()
		if args.help:
			console.Banner()
			arg_parse.print_help()
			sys.exit(0)
		elif args.update:
			pass
		elif not args.url:
			console.Banner()
			arg_parse.print_usage()
			sys.exit(0)
		return args
	
	def run(self, spider_parser):
		a=self.arg
		try:
			if a.raw:
				raw=open(a.raw).read()
			else:
				raw=a.raw
		except Exception as e:
			console.Error(e)
			raise
		
		spider_parser(
		debug=a.view,
		url=a.url,
		raw=raw,
		host=a.host,
		name=a.name,
		hide_bar=a.bar,
		update=a.update,
		)
	
	def __init__(self):
		self.argparse=__import__("argparse")
		self.name=sys.argv[0]
		self.arg=self.ArgParse()
	
	def __repr__(self):
		return "Done"
	
	def __str__(self):
		return "Done"

main=Program()
args=main.arg
from core import parser
Request=parser.Request_settings(args)
parser.Request=Request
parser.proggress=proggress
try:
	main.run(parser.spider_parser)
except KeyboardInterrupt:
	proggress.stop()
	console.Log("Program has been stopped by the user.")
	sys.exit(0)
except Exception:
	proggress.stop()
	raise
