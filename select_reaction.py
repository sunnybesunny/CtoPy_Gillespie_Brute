#
# select_reaction.c
# 
 # Created on: Oct 23, 2015
     # Author: User1
# 

#include <stdio.h>              # This program simulates dynamics of affinity maturation in germinal centers 
##include <stdlib.h>
##include <math.h>
##include <time.h>	 	        /* for seeding the rd # generator */
##include <limits.h>
#include "header_gillespie.h"

select_reaction(P, num_RXN_curr, sum_propencity, randN){
	reaction = -1
	sp = 0.0
	randN = randN * sum_propencity
	for(i=0; i<num_RXN_curr; i++){
		sp += P[i]
		#printf("sp: %f\n", sp)
		if randN < sp:
        #printf("randN: %f\n",randN)
			reaction = i
			break

	return reaction
