#
# header_gillespie.h
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


def Sqr(a):	return (a)*(a)
def MIN(a,b):	return ((a)<(b)?(a):(b))
def MAX(a,b):	return ((a)>(b)?(a):(b))


# Define Parameters as macros
t	= 0.05	# total t span 
Type_spe	= 6  # # of Type of species: C_Ag,C_B*,C_Ic,C_IgG,C_IgM,T_fH 
Type_dose	= 4
num_RXN	= 5	# # of rxn
num_RXN_init	= 5 # # of rxn before t<6d
a	= 2			# Version 1 a=2
dose_per	= 1 # dosing period
Volume	= 0.000001 #volume of the lymph node, 1uL  

# Variables 
extern V[num_RXN][Type_spe] #stoichiometry matrix 
extern C[num_RXN]    # rate constant matrix c 
extern H_s[num_RXN] #Permutation matrix H  
extern S[Type_spe][Type_dose]  # state_matrix S: need to be dynamically allocated, maybe not
extern P[num_RXN] # propensity 

#function prototypes

#endif # HEADER_GILLESPIE_H_ 
