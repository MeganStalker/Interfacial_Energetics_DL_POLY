#!/bin/bash

# Script 1/6

######################
## By Megan Stalker ##
######################

# This bundle of shell and python scripts determines the interfacial energy and work of adhesion (in Jm-2) for a given system from DL_POLY simulations.

# 1.	1gocoavint.sh:	Goes through each folder and extracts the relevant data and calls the relevant scripts and cleans up

# 2.	2extract.sh:	Extracts the necessary data from the relevant DL_POLY input (CONFIG, CONTROL) and output files (SOLVAT, OUTPUT) to cou_energies.out, vdw_energies.out, timestep.out, ratios.out, configenergies.out, volume.out. Calls the remaining scripts (3work.py, 4blockcoav.py and 5normalise.py)

# 3.	3work.py:	Calculates the instantaneous work of adhesion (in kcalmol-1) by combining the Coulombic and Van der waals energy and appends to work_adhesion_data.out

# 4.	4blockcoav.py:	Determines whether the instantaneous work of adhesion and configurational energy have converged using dlmontepython. The point of convergence and the correlation function is used to calculate the work of adhesion data and the interfacial energy 

# 5.	5normalise.py:	Calculates the work of adhesion and interfacial energy per unit area (KCalMol-1A-2)

# 6.	6calcint.py:	 Calculates the cellulose-vacuum, cellulose-water and water-vacuum interfacial energies (Jm-2) and the cellulose-water work of adhesion (Jm-2)as well as the corresponding uncertainties


############
# CLEAN-UP #
############

mv int_e/scripts/* .
rm -rf int_e/

# This script goes through each folder in the directory and performs an interfacial calculation

for D in *; do
    if [ -d "${D}" ]; then
	cp 2extract.sh $D/prod/
	cp 3work.py $D/prod/
	cp 5normalise.py $D/prod/
	cp 4blockcoav.py $D/prod/
	cd $D/prod/
	pwd
	./2extract.sh	
	cd ../
	pwd
	test=$(pwd | awk -F'[/=]' '{print $NF}')

	mv ./prod/work_output/data/normalised_work_adhesion_energies.txt ./prod/work_output/data/normalised_work_adhesion_energies_$test
	cp ./prod/work_output/data/normalised_work_adhesion_energies_* ../

	mv ./prod/work_output/data/normalised_interfacial_energies.txt ./prod/work_output/data/normalised_interfacial_energies_$test
	cp ./prod/work_output/data/normalised_interfacial_* ../

	cd ../
	pwd
    fi
done

python 6calcint.py

#########
#CLEANUP#
#########

mkdir int_e
cd int_e
mkdir graphs
mv ../*.pdf ./graphs/

mkdir data
mv ../normalised_energies* ./data/
mv ../timestep.out ./data/
mv ../interfacialenergies.txt ./data/
mv ../interfacial_energy ./data/
mv ../normalised* ./data/

mkdir scripts
mv ../*.py ./scripts
mv ../*.sh ./scripts
