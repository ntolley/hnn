'''
init.py

Starting script to run NetPyNE-based HNN model.

Usage:
    python init.py # Run simulation, optionally plot a raster

MPI usage:
    mpiexec -n 4 nrniv -python -mpi init.py

Contributors: salvadordura@gmail.com
'''

from netpyne import sim
from utils import setCfgFromFile



# Parameters file to read
cfgFile = '../param/ERPYes100Trials.param'      # ERP
# cfgFile = '../param/AlphaAndBeta.param'         # Alpha and Beta
#cfgFile = '../param/gamma_L5ping_L2ping.param'  # Gamma

# Import simConfig and set parameters from file
from cfg import cfg
cfg = setCfgFromFile(cfgFile, cfg)

# Import netParams
from netParams import netParams

# Create, simulate and analyze model
sim.createSimulateAnalyze(simConfig=cfg, netParams=netParams) 
