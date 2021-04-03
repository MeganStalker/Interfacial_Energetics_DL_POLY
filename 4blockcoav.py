#!/bin/python

# Script 4/6

######################
## By Megan Stalker ##
######################

# This python script determines whether the simulation has converged, the point of convergence and the correlation function for the work of adhesion data and the configurational energy data using dlmontepython 

###########
# MODULES #
###########

# Imports all the necessary modules

import dlmontepython.simtask.analysis as analysis
import numpy as np
import logging

#######################
# 1. WORK OF ADHESION #
#######################

#####################
# 1.1. LOAD IN DATA #
#####################

# Extracts the work of adhesion data from work_adhesion_data.out and stores as work

work=np.loadtxt("./work_adhesion_data.out")

#########################
# 1.2. CORRELATION TIME #
#########################

# Uses the function analysis to determine if the work of adhesion data has converged and the point of covnergence

checktimes=np.arange(0, 1, 0.025)
work_flatslice, work_slicepos = analysis.equilibration_test(work, checktimes)

print('The checktimes grid is', checktimes)
print (work_flatslice) # true/false, is the slice flat?
print (work_slicepos)  # from which data point is the data flat?

# Calculate the autocorrelation time (tau) of the work of adhesion data

work_s = analysis.inefficiency(work[work_slicepos:])
work_tau = -1.0/np.log(1.0-2.0/(work_s+1.0)) 
print(work_tau) # the correlation time 

if work_tau <= 1:
	work_tau=1

work_corr=int(work_tau)
print(work_corr)

##########################
# 1.3 BLOCK CO-AVERAGING #
##########################

# use the function block_average to block co-average the work of adhesion data from the position of the flatslice, in sizes of corr (tau - the correlation time)

work_corr_average=analysis.block_averages(work[work_slicepos:], work_corr)
print(work_corr_average) # prints an array of the averages of each block
print(len(work_corr_average)) # prints the length of the array

work_average_average=(sum(work_corr_average)/len(work_corr_average)) # determines the average across all blocks
print(work_average_average) 

work_average_error=np.std(work_corr_average) # determines the standard deviation across all blocks
print(work_average_error)

#####################
# 1.4 DATA PRINTING #
#####################

filename = "work_adhesion_av.out"
file = open(filename, 'w')

line_1 = ["The work of adhesion is ","", "kcal mol-1:" '\n']
file.writelines(line_1),

line_2 = [str(work_average_average),"(+/-)", str(work_average_error), '\n']
file.writelines(line_2),

line_3 = ["The system equilibrilates after"," ",str(work_slicepos)," ", "steps" '\n']
file.writelines(line_3),


line_4 = ["The correlation time is:"," ",str(work_tau)," ", '\n']
file.writelines(line_4),

file.close()

filename = "work_convergence_time"

file = open(filename, 'w')
line_1 = [str(work_slicepos) , '\n']
file.writelines(line_1),

line_2 = ["500" , '\n']
file.writelines(line_2),

line_3 = [str(len(work)) , '\n']
file.writelines(line_3),
file.close()


#########################
# 2. INTERFACIAL ENERGY #
#########################

#####################
# 2.1. LOAD IN DATA #
#####################

# Extracts the configurational energy data from configenergies.out and stores as pot

pot=np.loadtxt("./configenergies.out")

#########################
# 2.2. CORRELATION TIME #
#########################

# Uses the function analysis to determine if the configurational energy data has converged and the point of convergence

checktimes=np.arange(0, 1, 0.025)
pot_flatslice, pot_slicepos = analysis.equilibration_test(pot, checktimes)

print('The checktimes grid is', checktimes)
print (pot_flatslice) # true/false, is the slice flat?
print (pot_slicepos)  # from which data point is the data flat?

# Calculate the autocorrelation time (tau) of the configurational energy 

pot_s = analysis.inefficiency(pot[pot_slicepos:])
pot_tau = -1.0/np.log(1.0-2.0/(pot_s+1.0)) 
print(pot_tau) # the correlation time 

if pot_tau <= 1:
	pot_tau=1

pot_corr=int(pot_tau)
print(pot_corr)

##########################
# 2.3 BLOCK CO-AVERAGING #
##########################

# use the function block_average to block co-average the data from the position of the flat slice, in sizes of corr (tau - the correlation time)

pot_corr_average=analysis.block_averages(pot[pot_slicepos:], pot_corr)
print(pot_corr_average) # prints an array of the averages of each block
print(len(pot_corr_average)) # prints the length of the array

pot_average_average=(sum(pot_corr_average)/len(pot_corr_average)) # determines the average across all blocks
print(pot_average_average) 

pot_average_error=np.std(pot_corr_average) # determines the standard deviation across all blocks
print(pot_average_error)

#####################
# 2.4 DATA PRINTING #
#####################

filename = "interfacial_av.out"
file = open(filename, 'w')

line_1 = ["The interfacial energy is ","", "kcal mol-1:" '\n']
file.writelines(line_1),

line_2 = [str(pot_average_average),"(+/-)", str(pot_average_error), '\n']
file.writelines(line_2),

line_3 = ["The system equilibrilates after"," ",str(pot_slicepos)," ", "steps" '\n']
file.writelines(line_3),


line_4 = ["The correlation time is:"," ",str(pot_tau)," ", '\n']
file.writelines(line_4),

file.close()

filename = "interfacial_convergence_time"

file = open(filename, 'w')
line_1 = [str(pot_slicepos) , '\n']
file.writelines(line_1),

line_2 = ["500" , '\n']
file.writelines(line_2),

line_3 = [str(len(pot)) , '\n']
file.writelines(line_3),
file.close()

