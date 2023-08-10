from distutils.core import setup
from Cython.Build import cythonize

setup(name="myclass",
      ext_modules=cythonize("myclass.pyx", compiler_directives={"language_level": "3"}))
