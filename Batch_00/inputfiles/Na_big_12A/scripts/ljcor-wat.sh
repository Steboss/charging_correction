#!/bin/bash

cd lambda-0.0000
~/sire.app/bin/somd-lj-tailcorrection -C ../../input/sim.cfg -l 0.00 -b "1.00 * gram / (centimeter*centimeter*centimeter)" -r traj000000001.dcd -s 100 1> ../freenrg-LJCOR-lam-0.000.dat 2> /dev/null

wait

cd ..
cd lambda-1.0000
~/sire.app/bin/somd-lj-tailcorrection -C ../../input/sim.cfg -l 1.00 -b "1.00 * gram / (centimeter*centimeter*centimeter)" -r traj000000001.dcd -s 100 1> ../freenrg-LJCOR-lam-1.000.dat 2> /dev/null
cd ..

wait

