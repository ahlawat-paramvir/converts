from ase.io import read, write
from ase.visualize import view
import os
import numpy as np

symbols = []
f = 0
g = 0

out_filename = './mol_6.extxyz'

in_filename = './all.extxyz'

atoms = read(in_filename, index=':')
x = len(atoms)

for i in range(x):
    frame = atoms[i]
    x = frame.get_all_distances()
    if (len(x) > 1):
        k = []
        j = 0
        for j in range(len(x)):
            k.append(np.min(x[j][np.nonzero(x[j])]))
        if (np.max(k)) < 6.0 :
#            symbols = symbols + atoms.get_chemical_symbols()
            try:
                frame.get_total_energy()
                if (np.min(abs(frame.get_forces())) != 0.00000):
                    write(out_filename, frame, append=True, format='extxyz')
            except:
                 pass
