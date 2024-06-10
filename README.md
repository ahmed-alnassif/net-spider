# Net-Spdier
This tool scrapes the source code of an HTML page, including all the content within it, such as external files like JavaScript, CSS, images, fonts, and more. Additionally, it analyzes the CSS files and extracts any external links found within them. The tool is designed to assist developers in understanding the code used by large companies, focusing specifically on front-end development. It only retrieves front-end code and does not handle back-end or server-side code.
<div align="center">
<img src="https://raw.githubusercontent.com/ahmed-alnassif/net-spider/main/static/img.jpeg" alt="Net-Spider"/>
</div>

# Installation
Packages needed for installation
# Arch Linux:
```bash
sudo pacman -Syu git python python-pip
```
# Fedora:
```bash
sudo dnf update
sudo dnf install git python python-pip
```

# Ubuntu or Debian:
```bash
sudo apt update
sudo apt install git python python-pip -y
```

# Termux (Android):
```bash
apt update
apt install git python -y
```

Installation
```bash
git clone --depth=1 https://github.com/ahmed-alnassif/net-spider.git
```
Installation packages python
```bash
cd net-spider
python -m pip install -r requirements.txt
# OR
python setup.py install
```
Run
```bash
python main.py -u [url]
# Example
python main.py -u https://example.com
```

# Usage
```bash
python main.py --help
```
```
  _____   __    _____     ________       ______________
___  | / /______  /_    __  ___/__________(_)_____  /____________
__   |/ /_  _ \  __/    _____ \___  __ \_  /_  __  /_  _ \_  ___/
_  /|  / /  __/ /_      ____/ /__  /_/ /  / / /_/ / /  __/  /
/_/ |_/  \___/\__/      /____/ _  .___//_/  \__,_/  \___//_/
                               /_/

Created By: Ahmed Al-Nassif  
Github: https://github.com/ahmed-alnassif  
E-mail: Mr.Ahmed.Nassif@gmail.com  
Facebook: https://fb.me/ahm3d.nassif  
Program version: 24.6.4  

usage: python main.py -u [url]

This project designed to retrieve the source code for a web page, including front-end elements such as JavaScript, CSS, images, and fonts.

Net-Spider:
  --help          Show usage and help parameters
  -u              Target URL (e.g. http://example.com)
  -d, --domain    Pull links from the primary website address only
  --name NAME     The name of the folder in which to save the site files
  --hide          Hide the progress bar [----]
  -v              Give more output.
  --page RAW      Parse an HTML file and retrieve all files from it
  --update        Automatically update the tool

Requests settings:
  --random-agent  Random user agent
  --mobile        make requests as mobile default: PC, Note: this option will active random agent
  --cookie        Set cookie (e.g {"ID": "1094200543"})
  --header        Set header (e.g {"User-Agent": "Chrome Browser"})
  --proxy PROXY   Set proxy (e.g. {"https":"https://10.10.1.10:1080"})
```

# Screenshots
<div align="center">
<img width="90%" src="https://raw.githubusercontent.com/ahmed-alnassif/net-spider/main/static/Screenshot.png" alt="screenshot tool net-spider"/>
<br/>
<img width="90%" src="https://raw.githubusercontent.com/ahmed-alnassif/net-spider/main/static/Screenshot_2.png" alt="screenshot tool net-spider"/>
<br/>
<img width="90%" src="https://raw.githubusercontent.com/ahmed-alnassif/net-spider/main/static/Screenshot_3.png" alt="net-spider WhatsApp"/>
</div>
