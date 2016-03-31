#
# header_gillespie.py
# no need of this file
#
 # Created on: Oct 20, 2015
     # Author: Sunny K
       # Pseudocode:
     	# Define 		time span t=[0,40] (day)
     	# Define 		Type-dose
     	# Define 		Num RXN
     	# Define 		Num RXN-init
     	# Define 		a Tfh expansion factor
     	# Define 		dose per
     	# Define 		Ag_dosing Matrix,F(dose_type,day)
     	# Define 		stoichiometric matrix v
     	# Initialize 	species #
     	# Initialize	rate constant matrix c,
     				# Permutation matrix h
     	# Initialize 	state_matrix S[type_spe][type_dose]
#
			# RXN:
			# 1. C_Ag --> 0
			# 2. C_IgM+C_Ag-->C_Ic
			# 3. C_IgG+C_Ag-->C_Ic
			# 4. C_B*-->C_IgG
			# 5. T_fh-->aT_fh (V1. a=2)
#

#ifndef HEADER_GILLESPIE_H
HEADER_GILLESPIE_H	= #include <stdio.h>              # This program simulates dynamics of affinity maturation in germinal centers
##include <stdlib.h>



# Variables
extern V[num_RXN][Type_spe] #stoichiometry matrix
extern C[num_RXN]    # rate constant matrix c
extern H_s[num_RXN] #Permutation matrix H
extern S[Type_spe][Type_dose]  # state_matrix S: need to be dynamically allocated, maybe not
extern P[num_RXN] # propensity

#function prototypes

#endif # HEADER_GILLESPIE_H_
