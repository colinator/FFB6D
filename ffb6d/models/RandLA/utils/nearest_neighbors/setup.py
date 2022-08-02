from distutils.core import setup
from distutils.extension import Extension
#from Cython.Distutils import build_ext
#import numpy

def buildit():
    from Cython.Distutils import build_ext
    return build_ext

def numpy_includes():
    import numpy as np
    return np.get_include()


ext_module = Extension(
    "nearest_neighbors",
    sources=["knn.pyx", "knn_.cxx",],  # source file(s)
    include_dirs=["./", numpy_includes()], #numpy.get_include()],
    language="c++",            
    extra_compile_args=["-std=c++11", "-fopenmp"],
    extra_link_args=["-std=c++11", '-fopenmp'],
)

setup(
    name = "KNNNanoFLANN",
    ext_modules = [ext_module],
    cmdclass = {'build_ext': buildit},
    install_requires=[
        'Cython',
        'numpy',
    ],
)
