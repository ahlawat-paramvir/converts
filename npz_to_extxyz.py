## most of this one is from Simon Batzner's one, adated a bit here and there
import numpy as np

from ase import Atoms
from ase.io import write
from ase.calculators.singlepoint import SinglePointCalculator

# read in npz file
in_filename = 'any.npz'
out_filename = 'nequip-data.extxyz'
data = np.load(in_filename)


# get data 
positions = data['xyz']
cells = data['lattice']
numbers = data['numbers']
energies = data['energy']
forces = data['gradients']
stress= data['stress']

# iterate over data and write continuously to extxyz file
for idx in range(len(positions)):
  curr_atoms = Atoms(
    # set atomic positions
    positions=positions[idx],
    # set cell in case it exists
    cell=cells[idx],
    # set chemica species, either by symbols or numbers
    numbers=data['numbers'], 
    pbc=True
  )
  
  # set calculator to assign targets
  calculator = SinglePointCalculator(curr_atoms, energy=energies[idx], forces=forces[idx])
  curr_atoms.calc = calculator
 
  write(out_filename, curr_atoms, format='extxyz', append=True)
