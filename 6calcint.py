#!/usr/bin/python

import Tkinter
import seaborn as sns
import numpy as np
from pylab import *

# Script 6/6

# This python script calculates the cellulose-vacuum, cellulose-water and water-vacuum interfacial energies (Jm-2) and the cellulose-water work of adhesion (Jm-2)as well as the corresponding uncertainties

#######################
# 1. WORK OF ADHESION #
#######################

#####################
# 1.1. LOAD IN DATA #
#####################

cell_wat_work_data=np.loadtxt('cell_wat/prod/work_output/data/normalised_work_adhesion_energies_cell_wat', dtype=None)
av_cell_wat_work=cell_wat_work_data[0]
stdev_cell_wat_work=cell_wat_work_data[1]

av_cell_wat_work_joules=av_cell_wat_work*4180
av_cell_wat_work_metre=av_cell_wat_work_joules*(10**20)
av_cell_wat_work_final=av_cell_wat_work_metre/(6.023*10**(23))

stdev_cell_wat_work_joules=stdev_cell_wat_work*4180
stdev_cell_wat_work_metre=stdev_cell_wat_work_joules*(10**20)
stdev_cell_wat_work_final=stdev_cell_wat_work_metre/(6.023*10**(23))

#########################
# 2. INTERFACIAL ENERGY #
#########################

#####################
# 2.1. LOAD IN DATA #
#####################

#######################################################
# 2.1.1. CELLULOSE CELLULOSE NORMALISED SYSTEM ENERGY #
#######################################################

#Extracts the normalised energy of the cellulose-cellulose interaction into a new array

cell_cell_data=np.loadtxt('normalised_interfacial_energies_cell_cell', dtype=None)
av_cell_cell=cell_cell_data[0]
stdev_cell_cell=cell_cell_data[1]

av_cell_cell_joules=av_cell_cell*4180
av_cell_cell_metre=av_cell_cell_joules*(10**20)
av_cell_cell_final=av_cell_cell_metre/(6.023*10**(23))

stdev_cell_cell_joules=stdev_cell_cell*4180
stdev_cell_cell_metre=stdev_cell_cell_joules*(10**20)
stdev_cell_cell_final=stdev_cell_cell_metre/(6.023*10**(23))

###################################################
# 2.1.2. CELLULOSE WATER NORMALISED SYSTEM ENERGY #
###################################################

#Extracts the normalised energy of the cellulose-water interaction into a new array

cell_wat_data=np.loadtxt('normalised_interfacial_energies_cell_wat', dtype=None)
av_cell_wat=cell_wat_data[0]
stdev_cell_wat=cell_wat_data[1]

av_cell_wat_joules=av_cell_wat*4180
av_cell_wat_metre=av_cell_wat_joules*(10**20)
av_cell_wat_final=av_cell_wat_metre/(6.023*10**(23))

stdev_cell_wat_joules=stdev_cell_wat*4180
stdev_cell_wat_metre=stdev_cell_wat_joules*(10**20)
stdev_cell_wat_final=stdev_cell_wat_metre/(6.023*10**(23))



###############################################
# 2.1.3. WATER WATER NORMALISED SYSTEM ENERGY #
###############################################

#Extracts the normalised energy of the water-water interaction into a new array

wat_wat_data=np.loadtxt('normalised_interfacial_energies_wat_wat', dtype=None)
av_wat_wat=wat_wat_data[0]
stdev_wat_wat=wat_wat_data[1]

av_wat_wat_joules=av_wat_wat*4180
av_wat_wat_metre=av_wat_wat_joules*(10**20)
av_wat_wat_final=av_wat_wat_metre/(6.023*10**(23))

stdev_wat_wat_joules=stdev_wat_wat*4180
stdev_wat_wat_metre=stdev_wat_wat_joules*(10**20)
stdev_wat_wat_final=stdev_wat_wat_metre/(6.023*10**(23))


#############################################
# 2.1.4. WATER VAC NORMALISED SYSTEM ENERGY #
#############################################

#Extracts the normalised energy of the water-vac interaction into a new array

wat_vac_data=np.loadtxt('normalised_interfacial_energies_wat_vac', dtype=None)
av_wat_vac=wat_vac_data[0]
stdev_wat_vac=wat_vac_data[1]

av_wat_vac_joules=av_wat_vac*4180
av_wat_vac_metre=av_wat_vac_joules*(10**20)
av_wat_vac_final=av_wat_vac_metre/(6.023*10**(23))

stdev_wat_vac_joules=stdev_wat_vac*4180
stdev_wat_vac_metre=stdev_wat_vac_joules*(10**20)
stdev_wat_vac_final=stdev_wat_vac_metre/(6.023*10**(23))


#################################################
# 2.1.5. CELLULOSE VAC NORMALISED SYSTEM ENERGY #
#################################################

#Extracts the normalised energy of the cellulose-vac interaction into a new array

cell_vac_data=np.loadtxt('normalised_interfacial_energies_cell_vac', dtype=None)
av_cell_vac=cell_vac_data[0]
stdev_cell_vac=cell_vac_data[1]

av_cell_vac_joules=av_cell_vac*4180
av_cell_vac_metre=av_cell_vac_joules*(10**20)
av_cell_vac_final=av_cell_vac_metre/(6.023*10**(23))

stdev_cell_vac_joules=stdev_cell_vac*4180
stdev_cell_vac_metre=stdev_cell_vac_joules*(10**20)
stdev_cell_vac_final=stdev_cell_vac_metre/(6.023*10**(23))


####################################
# 2.2. INTERFACIAL ENERGY AVERAGES #
####################################

######################################################
# 2.2.1. CELLULOSE WATER INTERFACIAL ENERGY AVERAGES #
######################################################

cw_interfacial_final_av=(av_cell_wat_final)-(av_cell_cell_final*0.5)-(av_wat_wat_final*0.5)

#######################################################
# 2.2.2. CELLULOSE VACUUM INTERFACIAL ENERGY AVERAGES #
#######################################################

cv_interfacial_final_av=(av_cell_vac_final)-(av_cell_cell_final*0.5)

###################################################
# 2.2.3. WATER VACUUM INTERFACIAL ENERGY AVERAGES #
###################################################

wv_interfacial_final_av=(av_wat_vac_final)-(av_wat_wat_final*0.5)

####################
# 3. UNCERTAINTIES #
####################

##################################################
# 3.2.1. CELLULOSE WATER INTERFACIAL UNCERTAINTY #
##################################################

stdev_cw_interfacial=sqrt((stdev_cell_wat_final)**2+(0.5*stdev_cell_cell_final)**2+(0.5*stdev_wat_wat_final)**2)


###################################################
# 3.2.2. CELLULOSE VACUUM INTERFACIAL UNCERTAINTY #
###################################################

stdev_cv_interfacial=sqrt((stdev_cell_vac_final)**2+(0.5*stdev_cell_cell_final)**2)

###############################################
# 3.2.3. WATER VACUUM INTERFACIAL UNCERTAINTY #
###############################################

stdev_wv_interfacial=sqrt((stdev_wat_vac_final)**2+(0.5*stdev_wat_wat_final)**2)


###################
# 4 DATA PRINTING #
###################

filename = "normalised_cw_interfacial.txt"
file = open(filename, 'w')

line_1 = [str(cw_interfacial_final_av), '\n']
file.writelines(line_1),

line_2 = [str(stdev_cw_interfacial)]
file.writelines(line_2),

file.close()


filename = "normalised_cv_interfacial.txt"
file = open(filename, 'w')

line_1 = [str(cv_interfacial_final_av), '\n']
file.writelines(line_1),

line_2 = [str(stdev_cv_interfacial)]
file.writelines(line_2),

file.close()


filename = "normalised_wv_interfacial.txt"
file = open(filename, 'w')

line_1 = [str(wv_interfacial_final_av), '\n']
file.writelines(line_1),

line_2 = [str(stdev_wv_interfacial)]
file.writelines(line_2),

file.close()


filename = "final_work_adhesion_energies_cell_wat.txt"
file = open(filename, 'w')

line_1 = [str(av_cell_wat_work_final), '\n']
file.writelines(line_1),

line_2 = [str(stdev_cell_wat_work_final)]
file.writelines(line_2),

file.close()


filename = "final_interfacial_energies_cell_cell.txt"
file = open(filename, 'w')

line_1 = [str(av_cell_cell_final), '\n']
file.writelines(line_1),

line_2 = [str(stdev_cell_cell_final)]
file.writelines(line_2),

file.close()


filename = "final_interfacial_energies_cell_vac.txt"
file = open(filename, 'w')

line_1 = [str(av_cell_vac_final), '\n']
file.writelines(line_1),

line_2 = [str(stdev_cell_vac_final)]
file.writelines(line_2),

file.close()


filename = "final_interfacial_energies_cell_wat.txt"
file = open(filename, 'w')

line_1 = [str(av_cell_wat_final), '\n']
file.writelines(line_1),

line_2 = [str(stdev_cell_wat_final)]
file.writelines(line_2),

file.close()


filename = "final_interfacial_energies_wat_wat.txt"
file = open(filename, 'w')

line_1 = [str(av_wat_wat_final), '\n']
file.writelines(line_1),

line_2 = [str(stdev_wat_wat_final)]
file.writelines(line_2),

file.close()


filename = "final_interfacial_energies_wat_vac.txt"
file = open(filename, 'w')

line_1 = [str(av_wat_vac_final), '\n']
file.writelines(line_1),

line_2 = [str(stdev_wat_vac_final)]
file.writelines(line_2),

file.close()

