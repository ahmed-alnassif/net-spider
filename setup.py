from setuptools import setup
from core.console import console

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="Net-Spider",
    py_modules=["net-spider"],
    entry_points={},
    scripts=('main.py',),
    version=console.Version(),
    description="Pull source page front-end all source css, javascript, images, fonts",
    long_description=long_description,
    author="Ahmed Al-Nassif",
    author_email="mr.ahmed.nassif@gmail.com",
    url="https://github.com/ahmed-alnassif/net-spider",
    download_url="https://github.com/ahmed-alnassif/net-spider",
    keywords=["get source page", "html", "css", "javascript", "front-end", "net-spider"],
    license="MIT",
    install_requires=["requests", "bs4", "fake-useragent"],
)
