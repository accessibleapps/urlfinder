from setuptools import setup, find_packages
from urlfinder import __doc__, __version__

setup(
 name = 'urlfinder',
 version = __version__,
 description = __doc__,
 py_modules = ['urlfinder',],
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'Topic :: Software Development :: Libraries',
 ],
)
