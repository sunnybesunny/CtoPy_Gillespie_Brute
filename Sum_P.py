#
# sum_prop.c
# 
 # Created on: Oct 23, 2015
     # Author: User1
# 

##include <stdio.h>              /* This program simulates dynamics of affinity maturation in germinal centers */
##include <stdlib.h>
##include <math.h>
##include <time.h>	 	        /* for seeding the rd # generator */
##include <limits.h>
#include "header_gillespie.h"

def Sum_P(P,num_RXN_curr):
	sum_prop=0

	for i in range(num_RXN_curr):
			sum_prop = sum_prop+P[i]

	return sum_prop

#/////////////////////////////////////////////////////////////////////////////////
#//		Validation
#					printf("Sum_P.prop\n %e \n",sum_prop)
#
#/////////////////////////////////////////////////////////////////////////////////


