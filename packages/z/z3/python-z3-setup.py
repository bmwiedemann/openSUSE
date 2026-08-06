import os

from setuptools import setup


setup(
    name="z3-solver",
    version=os.environ["Z3_VERSION"],
    description="Python bindings for the Z3 theorem prover",
    license="MIT",
    packages=["z3"],
    include_package_data=False,
)
