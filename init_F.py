#
# init_F.c
#
 # Created on: Oct 21, 2015
     # Author: Sunny K
     # reads in text file f
     # store dosing schedule as F[dose_per][Type_dose]
#
#include <stdio.h>              # This program simulates dynamics of affinity maturation in germinal centers
##include <stdlib.h>
##include <math.h>
##include <time.h>	 	        /* for seeding the rd # generator */
#include "header_gillespie.h"
#include <errno.h>


def init_F(F_curr):

	with open('F_dosing_schedule.txt','r') as f:
		F_curr=[x.strip().split('\t') for x in f]

# convert the string to a long int

# 					 Validation
#			 		 printf("%e %e %e %e\n",F_curr[i][0],F_curr[i][1],F_curr[i][2],F_curr[i][3])

	print F_curr
	return F_curr
