#!/usr/bin/python

# Script 3/6

######################
## By Megan Stalker ##
######################

# This python script sums the values of the Coulombic and van der Waals energy at each timestep (extracted using extract.sh) to give the instantaneous work of adhesion (in kcalmol-1) and appends to work_adhesion_data.out 

###########
# MODULES #
###########

# Imports all the necessary modules

import seaborn as sns
import numpy as np
from pylab import *

####################
# WORK OF ADHESION #
####################

# Extracts the values of the Coulombic and van der Waals energy at each timestep

cou=np.loadtxt('cou_energies.out', dtype=None)
vdw=np.loadtxt('vdw_energies.out', dtype=None)

# Calculates the instantaneous work of adhesion (in kcalmol-1) and appends to work_adhesion_data.out

work_adhesion = []
for i in range(len(cou)):
	work_adhesion.append(cou[i]+vdw[i])

np.savetxt('work_adhesion_data.out', work_adhesion)





