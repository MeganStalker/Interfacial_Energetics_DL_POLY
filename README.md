# Interfacial_Energetics_DL_POLY

This bundle of shell and python scripts determines the interfacial energy and work of adhesion (in Jm-2) for a given system from DL_POLY simulations.

**1.	1gocoavint.sh**	

* Goes through each folder and extracts the relevant data
* Calls the relevant scripts
* Tidies up the workspace

**2. 2extract.sh**

* Extracts the necessary data from the relevant DL_POLY input (CONFIG, CONTROL) and output files (SOLVAT, OUTPUT)
* Appends to cou_energies.out, vdw_energies.out, timestep.out, ratios.out, configenergies.out, volume.out 
* Calls the remaining scripts (3work.py, 4blockcoav.py and 5normalise.py)

**3.	3work.py**	

* Calculates the instantaneous work of adhesion (in kcal mol<sup>-1</sup>) by combining the Coulmbic and Van der waals energy
* Appends to work_adhesion_data.out

**4.	4blockcoav.py**	

* Determines whether the instantaneous work of adhesion and configurational energy have converged using [dlmontepython](https://gitlab.com/dl_monte/dlmontepython).
* The point of convergence and the correlation function is used to calculate the work of adhesion data and the interfacial energy 

**5.	5normalise.py**	

* The average work of adhesion and interfacial energy per unit area (kcal mol<sup>-1</sup> Å<sup>-2</sup>)
* The associated standard error for the average work of adhesion and interfacial energy per unit area (kcal mol<sup>-1</sup> Å<sup>-2</sup>)

**6.	6calcint.py**
* Calculates the cellulose-vacuum, cellulose-water and water-vacuum interfacial energies (J m<sup>-2</sup>) and the cellulose-water work of adhesion (J m<sup>-2</sup>) as well as the corresponding uncertainties
