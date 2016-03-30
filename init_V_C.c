/*
 * init_V_C.c
 *
 *  Created on: Oct 21, 2015
 *      Author: User1
 */
//#include <stdio.h>              /* This program simulates dynamics of affinity maturation in germinal centers */
//#include <stdlib.h>
//#include <math.h>
//#include <time.h>	 	        /* for seeding the rd # generator */
//#include <limits.h>
#include "header_gillespie.h"

void init_V_C(double V_curr[][Type_spe], double C_curr[],double C_ref[],double V_ref[][Type_spe]){

	int i,j;
	for (i=0;i<num_RXN; i++)
			{
				C_curr[i]= C_ref[i];

//				Validation
//				printf("%f\n ",C_curr[i]);

					for (j=0; j<Type_spe; j++)
					{
						V_curr[i][j]= V_ref[i][j]; /*Why oh why??? */

//						Validation
//						printf("%f\n",V_curr[i][j]);
					}



			}

}
