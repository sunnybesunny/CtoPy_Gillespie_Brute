#
# Calc_P.c
#
 # Created on: Oct 22, 2015
     # Author: Sunny K
#

##include <stdio.h>              /* This program simulates dynamics of affinity maturation in germinal centers */
##include <stdlib.h>
##include <math.h>
##include <time.h>	 	        /* for seeding the rd # generator */
##include <limits.h>
#include "header_gillespie.h"
import numpy as np
def Calc_P( H_curr,C_curr, P_curr):
	P_curr=  H_curr*C_curr
	return P_curr
        #printf("Calc_P %f\n",P_curr[i])
#/////////////////////////////////////////////////////////////////////////////////
#//			Validation
#			for(i=0;i<num_RXN;i++){
#				printf("Calc_P.P\n %e \n",P_curr[i])
#			}
#/////////////////////////////////////////////////////////////////////////////////
