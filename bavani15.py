import sys
import importlib
import pip
from pip._internal import main
import pkg_resources
fileloc=r"D:\Bhavani\python\source.py"
print(fileloc)
tummyArray=[]
build_in_mod=sys.modules
#print(build_in_mod)
installed = [pkg.key for pkg in pkg_resources.working_set]
print(installed)
pkgs=[]
with open(fileloc,'r') as t:

    for lines in t:
        target = "import"
        tummyArray=lines.split()
        if 'import' in lines and "#" not in lines:
            for i,w in enumerate(tummyArray):
                if w == target:
                     check = tummyArray[i+1]
            if check not in build_in_mod and check.lower() not in installed:
                pkgs.append(check)

if len(pkgs) is not 0:
    print(pkgs)
    main(['install'] + pkgs)
    print("******************")
else:
    print("All the Packages are installed...")




         
