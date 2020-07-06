import sys
import importlib
import pip
import pkg_resources
tummyArray=[]
build_in_mod=sys.modules
#print(build_in_mod)
installed = [pkg.key for pkg in pkg_resources.working_set]
pkgs=[]
with open('app.py','r') as t:

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
    pip.main(['install'] + pkgs)
    print("******************")
else:
    print("All the Packages are installed...")




         
