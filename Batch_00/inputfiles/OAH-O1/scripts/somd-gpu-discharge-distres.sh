#!/bin/bash
#SBATCH -o somd-array-gpu-%A.%a.out
#SBATCH -p Tesla
#SBATCH -n 1
#SBATCH --gres=gpu:1
#SBATCH --time 48:00:00
#SBATCH --array=0-10

module load cuda/7.5

echo "CUDA DEVICES:" $CUDA_VISIBLE_DEVICES

lamvals=( 0.000 0.100 0.200 0.300 0.400 0.500 0.600 0.700 0.800 0.900 1.000 )
lam=${lamvals[SLURM_ARRAY_TASK_ID]}

if [ "$SLURM_ARRAY_TASK_ID" -eq "0" ]
then
    cat ../input/distres >> ../input/sim.cfg
fi

sleep 5


echo "lambda is: " $lam

mkdir lambda-$lam
cd lambda-$lam

export OPENMM_PLUGIN_DIR=/home/julien/sire.app/lib/plugins/

srun /home/steboss/sire_hbonds/sire.app/bin/somd-freenrg -C ../../input/sim.cfg -l $lam -p CUDA
cd ..

wait


