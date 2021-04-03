# Interfacial_Energetics_DL_POLY

This bundle of shell and python scripts determines the interfacial energy and work of adhesion (in Jm-2) for a given system from DL_POLY simulations.

**1.	1gocoavint.sh**	

* Goes through each folder and extracts the relevant data
* Calls the relevant scripts
* Tidies up the workspace

**2. 2extract.sh**

* Extracts the necessary data from the relevant DL_POLY input (CONFIG, CONTROL) and output files (SOLVAT, OUTPUT)
* Appends the data to the cou_energies.out, vdw_energies.out, timestep.out, ratios.out, configenergies.out and volume.out output files
* Calls the remaining scripts (3work.py, 4blockcoav.py and 5normalise.py)

**3.	3work.py**	

* Calculates the instantaneous work of adhesion (in kcal mol<sup>-1</sup>) by combining the Coulmbic and Van der waals energy
* Appends the instantaneous work of adhesion to the work_adhesion_data.out output file

**4.	4blockcoav.py**	

* Determines whether the instantaneous work of adhesion and configurational energy have converged using [dlmontepython](https://gitlab.com/dl_monte/dlmontepython).
* The point of convergence and the correlation function is used to calculate the work of adhesion data and to estimate the interfacial energy 

**5.	5normalise.py**	

* Calculates the average work of adhesion and estimates the interfacial energy per unit area (kcal mol<sup>-1</sup> Å<sup>-2</sup>)
* Calculates the associated standard error for the average work of adhesion and interfacial energy per unit area (kcal mol<sup>-1</sup> Å<sup>-2</sup>)

**6.	6calcint.py**

* Estimates the average cellulose-cellulose, cellulose-vacuum, cellulose-water, water-vacuum, water-water system energies (J m<sup>-2</sup>) as well as the corresponding uncertainties and appends to the relevant output files
* Calculates the average cellulose-water work of adhesion (J m<sup>-2</sup>) and estimates the average cellulose-vacuum, cellulose-water and water-vacuum interfacial energies (J m<sup>-2</sup>) as well as the corresponding uncertainties and appends to the relevant output files
