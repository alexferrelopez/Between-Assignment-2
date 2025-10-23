from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "arithmetic",
        ["bindings.cpp", "arithmetic.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++"
    )
]

setup(
    name="arithmetic",
    description="C++ arithmetic wrapped for Python",
    ext_modules=ext_modules,
)