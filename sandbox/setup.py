from distutils.core import setup
from Cython.Build import cythonize

# setup(name="cy_example", ext_modules=cythonize("cy_example.pyx", compiler_directives={"language_level": "3"}))
setup(name="cy_test", ext_modules=cythonize("cy_test.pyx", compiler_directives={"language_level": "3"}))