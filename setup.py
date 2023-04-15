import os
from setuptools import setup, Extension


setup(
    name="lanms-nova",
    version="1.0.3",
    author="Andranik Sargsyan",
    author_email="and.sargsyab@yahoo.com",
    description="lanms-nova is a python binding for LANMS - Locality-Aware Non-Max Suppression",
    install_requires=["numpy"],
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    packages=["lanms"],
    include_package_data=True,
    ext_modules=[
        Extension(
            name="lanms.lanmslib",
            sources=[
                os.path.join("src", "lanmslib.cpp"),
                os.path.join("src", "include", "clipper", "clipper.cpp")
            ],
            include_dirs=[os.path.join("src", "include")],
            language="c++",
            undef_macros=["NDEBUG"],
        ),
    ],
    zip_safe=False,
    license="GPL",
    keywords=["NMS", "LANMS"],
    url="https://github.com/AndranikSargsyan/lanms-nova",
)
