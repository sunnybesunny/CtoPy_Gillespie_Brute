/*
 * select_reaction.c
 *
 *  Created on: Oct 23, 2015
 *      Author: User1
 */

#include <stdio.h>              /* This program simulates dynamics of affinity maturation in germinal centers */
//#include <stdlib.h>
//#include <math.h>
//#include <time.h>	 	        /* for seeding the rd # generator */
//#include <limits.h>
#include "header_gillespie.h"

int select_reaction(double P[], int num_RXN_curr, double sum_propencity, double randN){
	int reaction = -1;
	double sp = 0.0;
	int i;
	randN = randN * sum_propencity;
	for(i=0; i<num_RXN_curr; i++){
		sp += P[i];
		//printf("sp: %f\n", sp);
		if(randN < sp){
        //printf("randN: %f\n",randN);
			reaction = i;
			break;
		}
	}

	return reaction;
}
