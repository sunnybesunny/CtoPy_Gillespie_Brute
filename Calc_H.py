#
# Calc_H.c
# 
 # Created on: Oct 20, 2015
     # Author: Sunny Kang
		# Calculate propensity,H based on current state,S
		# Pseudocode:
     	# Initialize 	H
			# H: [S[0],S[4]*S[0], S[3]*S[0],S[1],S[5]]
			# return H
# 
##include <stdio.h>              /* This program simulates dynamics of affinity maturation in germinal centers */
##include <stdlib.h>
##include <math.h>
##include <time.h>	 	        /* for seeding the rd # generator */
##include <limits.h>
#include "header_gillespie.h"

def Calc_H(S_curr[Type_dose], H_curr,j):
	{

		H_curr[0] = S_curr[0][j]
		H_curr[1] =S_curr[4][j]*S_curr[0][j] 
		H_curr[2] =S_curr[3][j]*S_curr[0][j] 
		H_curr[3] =S_curr[1][j] 
		H_curr[4] =S_curr[5][j] 

        #printf("%f\n",H_curr[2])
#/////////////////////////////////////////////////////////////////////////////////
#//		Validation
#		int i
#		for(i=0;i<num_RXN;i++){
#			printf("Calc_H.H\n %e \n",H_curr[i])
#		}
#/////////////////////////////////////////////////////////////////////////////////


