#!/bin/python

# Script 5/6

######################
## By Megan Stalker ##
######################

# This python script calculates the average work of adhesion and interfacial energy per unit area (kcalmol-1 A-2) and appends to work_adhesion.out and interfacial.out

###########
# MODULES #
###########

# Imports all the necessary modules

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#####################
# APPEND THE VOLUME #
#####################

# Extracts the volume from the file volume.out and reads into an array called volume

volume_data=np.loadtxt('volume.out', dtype=None)
volume=volume_data[0]

#####################
# APPEND THE HEIGHT #
#####################

# Extracts the height from the file height.out and reads into an array called height

height=np.loadtxt('height.out', dtype=None)

#######################
# APPEND THE ENERGIES #
#######################

# Extracts the work of adhesion and the interfacial energy from the files work_adhesion.out and interfacial.out and reads into the arrays work_adhesion_data and interfacial_data

work_adhesion_data=np.loadtxt('work_adhesion.out', dtype=None)
av_work_adhesion_energy=work_adhesion_data[0]
stdev_work_adhesion_energy=work_adhesion_data[1]

interfacial_data=np.loadtxt('interfacial.out', dtype=None)
av_interfacial_energy=interfacial_data[0]
stdev_interfacial_energy=interfacial_data[1]

######
#AREA#
######

# Calculates the area from the volume and the height

area=volume/height

#####################
# NORMALISED ENERGY #
#####################

# Calculates the average and standard deviation of the work of adhesion and the interfacial energy per unit area (Kcalmol-1 A-2) and append to the files normalised_work_adhesion_energies.txt and normalised_interfacial_energies.txt

norm_work_adhesion_av=av_work_adhesion_energy/area
norm_work_adhesion_std=stdev_work_adhesion_energy/area

filename = "normalised_work_adhesion_energies.txt"
file = open(filename, 'w')

line_1 = [str(norm_work_adhesion_av), '\n']
file.writelines(line_1),

line_2 = [str(norm_work_adhesion_std), '\n']
file.writelines(line_2),

file.close()

norm_interfacial_av=av_interfacial_energy/area
norm_interfacial_std=stdev_interfacial_energy/area

filename = "normalised_interfacial_energies.txt"
file = open(filename, 'w')

line_1 = [str(norm_interfacial_av), '\n']
file.writelines(line_1),

line_2 = [str(norm_interfacial_std), '\n']
file.writelines(line_2),

file.close()


