from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='arcade',
  version='1.0.0',
  description='a minimal and fun CUI mini games',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='',
  author='Sasi Vatsal',
  author_email='sasivatsal7122@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='arcade',
  packages=['arcade'],
  install_requires=[''],
)

