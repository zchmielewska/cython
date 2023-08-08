from distutils.core import setup
from Cython.Build import cythonize

setup(name="cython_particle",
      ext_modules=cythonize("cython_particle.pyx", compiler_directives={"language_level": "3"}))
