#Oct2016 Stefano Bosisio
#Script to create the effective running folder for all the inputfiles
import os,sys

def create_runsh(HG=False,G=False,ion=False):

    runner = open("run1.sh","w")

    runner.write("#!/bin/bash\n")
    if HG :#if bound is True, it means we have a protein
        runner.write('''cd bound\ncp -aL template run001\ncd run001\nbash runme.sh\ncd ../../\n''')
        runner.write('''cd free\ncp -a template run001\ncd run001\nbash runme.sh\n cd ../../\n''')
    elif G:
        runner.write('''cd free\ncp -a template run001\ncd run001\nbash runme.sh\n cd ../../\n''')
        runner.write('''cd vacuum\ncp -a template run001\ncd run001\nbash runme.sh\n cd ../../\n''')
    elif ion:
        runner.write('''cd free\ncp -a template run001\ncd run001\nbash runme.sh\n cd ../../\n''')
    else:
        print("ERROR! What inputfiles did you choose?")


#################
###MAIN SCRIPT###
#################

inputfiles = sys.argv[1]   #for f in inputfiles/*    e.g. Na_ion_X

if inputfiles[-1] == "/":
    inputfiles = inputfiles[:-1]

#print(inputfiles)
listdir = []
pert_name = inputfiles.split("/")[-1]
print(pert_name)

print("Creating directory...%s" %pert_name)
if not os.path.exists(pert_name):
    os.makedirs(pert_name)

print("Copying inputfiles")
for d in os.listdir(inputfiles):
    listdir.append(d)
    cmd = "cp -r  %s/%s %s/." %(inputfiles,d,pert_name)
    print(cmd)
    os.system(cmd)

print("Creationg run.sh script")

if "bound" in listdir:  #it means we have a hg system
    create_runsh(HG=True,G=False,ion=False)
elif "vacuum" in listdir :  #it means we want a hydration free energy
    create_runsh(HG=False,G=True,ion=False)
else: #if there is neither bound nor vacuum we are dealing with an ion (only free)
    create_runsh(HG=False,G=False,ion=True)


cmd ="mv run1.sh %s/." % pert_name
print(cmd)
os.system(cmd)
