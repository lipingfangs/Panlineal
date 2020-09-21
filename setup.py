from setuptools import setup, find_packages
import os
os.system("chmod 777 multiple.py goone.py Hapmerge.py bestref.py creatpangenome.py Panlineal.py Gathergoc.py ./script/mumlastzsvmu.sh mappingtools.py ./script/bosm.sh ./script/cadepth.sh")
setup(
      name="Panlinealv010",
      version="0.10",
      description="Panlineal",
      author="Fangping Li",
      license="LGPL",
      packages= find_packages(),
      scripts=["creatpangenome.py","./script/mumlastzsvmu.sh","multiple.py","./script/PAVsann.py","./script/bosm.sh","./script/cadepth.sh","mappingtools.py","Panlineal.py","Gathergoc.py","bestref.py","Hapmerge.py"],
      )
