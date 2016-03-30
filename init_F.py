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




	F_dosing_schedule=open("F_dosing_schedule.txt","r")

     if F_dosing_schedule == NULL:
        fprintf(stderr, "file open error\n")

	i=0

	   while fgets(line, 80, F_dosing_schedule) != NULL:
		 			 # get a line, up to 80 chars from fr.  done if NULL 
#			 	 	 printf(line)
                    printf("printing")
			 		 sscanf (line, "%lf %lf %lf %lf" % (&(F_curr[i][0]),&(F_curr[i][1]),&(F_curr[i][2]),&(F_curr[i][3])))
			 		 # convert the string to a long int 

# 					 Validation
#			 		 printf("%e %e %e %e\n",F_curr[i][0],F_curr[i][1],F_curr[i][2],F_curr[i][3])
			 		 i += 1

	  fclose(F_dosing_schedule)

