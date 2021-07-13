echo "Create funcX Endpoint for pyhf: pyhf-funcx"

module load python

conda env create -f m2-environment.yml
conda activate pyhf-funcx
# Currently having problems with pyzmq and funcx
python -m pip install --no-binary :all: --force-reinstall pyzmq
conda env list

module list
