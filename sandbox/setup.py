from distutils.core import setup
from Cython.Build import cythonize

# setup(name="cy_calculate", ext_modules=cythonize("cy_calculate.pyx", compiler_directives={"language_level": "3"}))
# setup(name="cy_model", ext_modules=cythonize("cy_model.pyx", compiler_directives={"language_level": "3"}))
setup(name="cy_calculate2", ext_modules=cythonize("cy_calculate2.pyx", compiler_directives={"language_level": "3"}))
