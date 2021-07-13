echo "Create funcX Endpoint for pyhf: pyhf-funcx"

module load python

conda env create -f m2-environment.yml
conda activate pyhf-expanse
conda env list

module list
