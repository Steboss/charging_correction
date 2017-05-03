#!/bin/bash

cd lambda-0.000
/home/steboss/sire.app/bin/somd-coul-tailcorrection -C ../../input/sim.cfg -l 0.00 -b "1.00 * gram / (centimeter*centimeter*centimeter)" -d 82.0 -e 78.3 -r traj000000001.dcd -s 100 1> ../freenrg-COULCOR.dat 2> /dev/null
cd ..
wait

# Extract final value
