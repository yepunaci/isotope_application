#! /bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -notify
#$ -o job.log -j y
#$ -l normal
#$ -N minimal

#add RMG-Py directory to PYTHONPATH (if desired):
source ~/.bash_rmg

#activate the Anaconda environment
source activate rmg_env

#run simulation
python ../../RMG-Py/rmg.py input.py

#deactivate the Anaconda environment
source deactivate
