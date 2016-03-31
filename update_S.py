#
# update_x.c
#
 # Created on: Oct 23, 2015
     # Author: User1
     # scheme type of dose
#
##include <stdio.h>              /* This program simulates dynamics of affinity maturation in germinal centers */
##include <stdlib.h>
##include <math.h>
##include <time.h>	 	        /* for seeding the rd # generator */
##include <limits.h>
#include "header_gillespie.h"

def update_S(S_curr, V_curr,reaction, scheme):

	S_curr[:,scheme] += V_curr[reaction,:]
	return S_curr
#/////////////////////////////////////////////////////////////////////////////////
#//		Validation
#		for(i=0;i<Type_spe;i++){
#					printf("update_S_before_update.S\n %e \n",S_curr[i][scheme])
#				}
#/////////////////////////////////////////////////////////////////////////////////
