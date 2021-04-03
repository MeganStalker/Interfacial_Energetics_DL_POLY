#!/bin/bash

# Script 2/6

######################
## By Megan Stalker ##
######################

# Extracts the Coulombic and van der Waals energy from the SOLVAT output file and appends to cou_energies.out and vdw_energies.out based on the format of the SOLVAT file.

# Extracts the volume, print ratios and the heights from the corresponding input files

# Extracts the configurational energy from the STATIS file and appends to configenergies.out

# Calls 3work.py and 4blockcoav.py

# Extracts the average and stdev of the work of adhesion and configurational energy from work_adhesion_av.out and  interfacial_av.out and appends to work_adhesion.out and interfacial.out

# Calls 5normalise.py 


############
# CLEAN-UP #
############

# Removes any files generated by previously running this script

mv work_output/scripts/* .
rm -rf work_output/
rm *txt *out 

#############
# UNZIPPING #
#############

# Unzips the necessary files

gunzip CONTROL.gz CONFIG.gz OUTPUT.gz FIELD.gz SOLVAT.gz

#######################
# 1. WORK OF ADHESION #
#######################

###############################################################
# 1.1. EXTRACTS THE COULOMBIC ENERGY AND VAN DER WAALS ENERGY #
###############################################################

# Extracts the Coulombic and van der Waals energy from the SOLVAT output file and appends to cou_energies.out and vdw_energies.out 

# Determines if there are dihedrals present ( dihedrals = T)

dihedrals=$(head -n 5 SOLVAT | tail -n 1 | awk '{print $5}')
echo $dihedrals

if [[ "$dihedrals" == "T" ]]
then

# Condition 1 - There are dihedrals in the system (dihedrals = T), there are 6 rows of data (cou = NR +5, vdw = NR +6)

        cou=$(awk '/timestep/{x = NR + 5}NR == x' SOLVAT | awk '{if (NF = 3) {print $2}}' | awk '{if ($1) print $0}')

        if [ -z "$cou" ]
        then
        # Condition 1.1 -  There are NOT any cross-terms, so need to extract NF=1 $1

                awk '/timestep/{x = NR + 5}NR == x' SOLVAT | awk '{if (NF = 1) {print $1}}' | awk '{if ($1) print $0}' >> cou_energies.out
                awk '/timestep/{x = NR + 6}NR == x' SOLVAT | awk '{if (NF = 1) {print $1}}' | awk '{if ($1) print $0}' >> vdw_energies.out
        else
        # Condition 1.2 -  There ARE cross-terms, so need to extract NF=3 $2

                awk '/timestep/{x = NR + 5}NR == x' SOLVAT | awk '{if (NF = 3) {print $2}}' | awk '{if ($1) print $0}' >> cou_energies.out
                awk '/timestep/{x = NR + 6}NR == x' SOLVAT | awk '{if (NF = 3) {print $2}}' | awk '{if ($1) print $0}' >> vdw_energies.out
        fi
else

# Condition 2 - There are NOT dihedrals in the system (dihedrals = F), there are 5 rows of data (cou = NR +4, vdw = NR +5)

        cou=$(awk '/timestep/{x = NR + 4}NR == x' SOLVAT | awk '{if (NF = 3) {print $2}}' | awk '{if ($1) print $0}')

        if [ -z "$cou" ]
        then
        # Condition 2.1 -  There are NOT any cross-terms, so need to extract NF=1 $1

                awk '/timestep/{x = NR + 4}NR == x' SOLVAT | awk '{if (NF = 1) {print $1}}' | awk '{if ($1) print $0}' >> cou_energies.out
                awk '/timestep/{x = NR + 5}NR == x' SOLVAT | awk '{if (NF = 1) {print $1}}' | awk '{if ($1) print $0}' >> vdw_energies.out
        else
	# Condition 2.2 -  There ARE cross-terms, so need to extract NF=3 $2

                awk '/timestep/{x = NR + 4}NR == x' SOLVAT | awk '{if (NF = 3) {print $2}}' | awk '{if ($1) print $0}' >> cou_energies.out
                awk '/timestep/{x = NR + 5}NR == x' SOLVAT | awk '{if (NF = 3) {print $2}}' | awk '{if ($1) print $0}' >> vdw_energies.out
        fi
fi


###############################
# 1.2. EXTRACTS THE TIMESTEPS #
###############################

# Extracts the timesteps from the SOLVAT output file and appends to timestep.out

awk '/timestep/' SOLVAT | awk '{print $2}' >> timestep.out

########################################
# EXTRACTS THE VARIOUS PRINTING RATIOS #
########################################

# Extracts the frequency of printing to the SOLVAT and OUTPUT file from the CONTROL input file and appends to ratios.out

grep "decompose" CONTROL | awk '{print $2}' >> ratios.out
grep "decompose" CONTROL | awk '{print $3}' >> ratios.out
grep "print" CONTROL | awk '{print $2}' | grep -v "rdf" >> ratios.out


#########################
# 2. INTERFACIAL ENERGY #
#########################

############################################
# 2.1. EXTRACTS THE CONFIGURATIONAL ENERGY #
############################################

#Finds a "landmark" in this case it is the number at the end of line 3 (the number of array elements)

x=$(grep -A1 "ENERGY UNITS" STATIS | grep -v "ENERGY UNITS" | awk '{ print $(NF)}' | head -1 )

#Uses this landmark to locate the configurational energy

grep -A1 -w  "$x"  STATIS | grep -v -w $x | grep -v "^--*$" | awk '{print $3}' >> ./configenergies.out

#######################
# 3 EXTRACTS THE AREA #
#######################

############################
# 3.1. EXTRACTS THE HEIGHT #
############################

# Extracts all unit cell dimensions from the CONFIG input file

ax=$(head -n 5 CONFIG | tail -n 3 | awk 'FNR == 1 {print $1}')
ay=$(head -n 5 CONFIG | tail -n 3 | awk 'FNR == 1 {print $2}')
ay=$(head -n 5 CONFIG | tail -n 3 | awk 'FNR == 1 {print $2}')
az=$(head -n 5 CONFIG | tail -n 3 | awk 'FNR == 1 {print $3}')

bx=$(head -n 5 CONFIG | tail -n 3 | awk 'FNR == 2 {print $1}')
by=$(head -n 5 CONFIG | tail -n 3 | awk 'FNR == 2 {print $2}')
bz=$(head -n 5 CONFIG | tail -n 3 | awk 'FNR == 2 {print $3}')

cx=$(head -n 5 CONFIG | tail -n 3 | awk 'FNR == 3 {print $1}')
cy=$(head -n 5 CONFIG | tail -n 3 | awk 'FNR == 3 {print $2}')
cz=$(head -n 5 CONFIG | tail -n 3 | awk 'FNR == 3 {print $3}')

vectors=( $ax $ay $az $bx $by $bz $cx $cy $cz)

# Determines the largest unit cell dimension and appends to height.out

maxvec=0.00

for vector in "${vectors[@]}" ; do
        if (( $(echo "$vector > $maxvec" |bc -l) )); then
                maxvec=$vector
        fi
done

echo $maxvec >> height.out

############################
# 3.2. EXTRACTS THE VOLUME #
############################

# Extracts the area from the OUTPUT output file and appends to volume.out

awk '/rolling/{x = NR + 2}NR == x' OUTPUT | awk '{print $1}' |  grep -v "^--*$" | grep -Ev "^$" >> volume.out

###################
# 4. CALL SCRIPTS #
###################

# Calls the remaining scripts (work_of_adhesion.py and doanalysis.py)

python 3work.py 
python 4blockcoav.py

# Extracts the average value and associated standard error for the work of adhesion from work_adhesion_av.out and appends to work_adhesion.out 

awk -F "(+/-)" 'FNR == 2 {print $1}' work_adhesion_av.out | awk -F "(" '{print $1}' >> work_adhesion.out
awk -F "(+/-)" 'FNR == 2 {print $2}' work_adhesion_av.out | awk -F ")" '{print $2}' >> work_adhesion.out

# Extracts the average value and associated standard error for the interfacial energy from interfacial_av.out and appends to interfacial.out 

awk -F "(+/-)" 'FNR == 2 {print $1}' interfacial_av.out | awk -F "(" '{print $1}' >> interfacial.out
awk -F "(+/-)" 'FNR == 2 {print $2}' interfacial_av.out | awk -F ")" '{print $2}' >> interfacial.out

# Calls the remaining scripts (interfacial.py and calculation.py)

python 5normalise.py

#########
#CLEANUP#
#########

# Tidies the data and the scripts into folders within work_output
# Removes any unneeded files

mkdir work_output
cd work_output
mkdir graphs
mv ../*.pdf ./graphs/

mkdir data
mv ../*out ../*txt ../*_time ./data
mv ../convergence_time ./data

mkdir scripts
mv ../*.py ./scripts
mv ../*.sh ./scripts

cd ../

#echo "work_adhesion"
#cat ./work_output/data/final_normalised_work_adhesion_energies.txt
#echo "interfacial"
#cat ./work_output/data/final_normalised_interfacial_energies.txt

