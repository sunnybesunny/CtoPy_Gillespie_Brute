/*
 * update_x.c
 *
 *  Created on: Oct 23, 2015
 *      Author: User1
 *      scheme type of dose
 */
//#include <stdio.h>              /* This program simulates dynamics of affinity maturation in germinal centers */
//#include <stdlib.h>
//#include <math.h>
//#include <time.h>	 	        /* for seeding the rd # generator */
//#include <limits.h>
#include "header_gillespie.h"

void update_S(double S_curr[][Type_dose], double V_curr[][Type_spe],int reaction, int scheme){
	int i;

	for(i=0; i<Type_spe; i++){
		S_curr[i][scheme] += V_curr[reaction][i];
	}

///////////////////////////////////////////////////////////////////////////////////
////		Validation
//		for(i=0;i<Type_spe;i++){
//					printf("update_S_before_update.S\n %e \n",S_curr[i][scheme]);
//				}
///////////////////////////////////////////////////////////////////////////////////

}
