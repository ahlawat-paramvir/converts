#!/usr/bin/tclsh

if {[catch {package require topotools 1.1} ver]} {
  vmdcon -error "$ver. This script requires at least TopoTools v1.1. Exiting..."
    quit
}

if {[catch {package require pbctools 2.3} ver]} {
  vmdcon -error "$ver. This script requires at least pbctools v2.3. Exiting..."
    quit
}
set id [mol new "slab.pdb"]
mol addfile "trajectory.dcd" waitfor all molid $id
set n_frames [molinfo $id get numframes]
for {set i 0} {$i < $n_frames} {incr i} {
  set mol [mol new slab.pdb waitfor all]
  mol addfile trajectory.dcd first $i last $i
  set newmol [::TopoTools::replicatemol $mol 1 1 1]
  animate write pdb $i.pdb $newmol
  mol delete all
}

#done. now exit vmd
quit
