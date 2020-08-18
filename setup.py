from setuptools import setup, find_packages
setup(
      name="creatpangenome",
      version="0.10",
      description="My test module",
      author="Fangping Li",
      license="LGPL",
      packages= find_packages(),
      scripts=["creatpangenome.py","mumlastzsvmu.sh","multiple.py"],
      )
