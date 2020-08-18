from setuptools import setup, find_packages
import os
os.system("chmod 777 multiple.py goone.py creatpangenome.py mumlastzsvmu.sh")
setup(
      name="creatpangenome",
      version="0.10",
      description="My test module",
      author="Fangping Li",
      license="LGPL",
      packages= find_packages(),
      scripts=["creatpangenome.py","mumlastzsvmu.sh","multiple.py"],
      )
