from distutils.core import setup
from Cython.Build import cythonize

setup(name="integrate", ext_modules=cythonize("integrate.pyx",
                                              compiler_directives={"language_level": 3}))
