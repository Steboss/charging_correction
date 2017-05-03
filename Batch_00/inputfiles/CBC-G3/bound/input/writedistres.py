#!/usr/bin/python

import os,sys,re
from parmed.amber import *

host_atoms = ["CLP:N4","CLP:N6","CLP:N8","CLP:N2"] 
guest_atoms = ["C6"]


# Load top/crd
top_file = "SYSTEM.top"
crd_file = "SYSTEM.crd"

base = AmberParm(top_file,crd_file)
# Select index of host_atom_names


host_idx = []

for val in host_atoms:
    res_atom = val.split(":")[1]             #atom of the resiude
    residue  = val.split(":")[0].strip()     #name of the residue
    #res_numb = int(re.split('(\d+)',residue)[1])  - 1  #number of the residue  -1 for mismatch between parmed and real life
    
    print("Residue name is %s" % (base.residues[1]))
    for atoms in base.residues[1]:
        print(base.residues[1])
        if atoms.name ==res_atom:

            print("Atom is %s whose index is %d" % (atoms.name,atoms.idx))
	    host_idx.append(atoms.idx)	

guest_idx = []

for val in guest_atoms:
    for atoms in base.residues[0]:
        if atoms.name == val:
            print("The guest atom is %s whose index is %d" % ( val, atoms.idx))
            guest_idx.append(atoms.idx)

# Write distres file

distres = "distance restraints dictionary = {(%s,%s):(4.00,10.0,2.00), (%s,%s):(4.00,10.0,2.00),(%s,%s):(4.00,10.0,2.00), (%s,%s):(4.00,10.0,2.00) }" % \
	( guest_idx[0],host_idx[0],guest_idx[0],host_idx[1],guest_idx[0],host_idx[2],guest_idx[0],host_idx[3])

print(distres)
stream = open("distres","w")
stream.write(distres)
stream.write("\n")
stream.close()

