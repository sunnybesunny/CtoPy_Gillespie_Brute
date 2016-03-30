#Gillespie_Fast.c
#
#  Created on: Oct 14, 2015
#      Author: Sunny K
#      Gillespie algorithm evolve during time domain with given v,c,H
#		Write the state evolution into the output
#
#		Return the most up to date species state
#
#      Pseudocode:
#      Initialize t_s = t(0), t_end= t(1)
#      t_new=t_s
#
#      Initialize species # from input N_init
#      Initialize the stoichiometric matrix v,
#      				rate constant matrix c,
#      				species state matrix h
#      While(t_new < t_end)
#      Calculate propensity (up until num_RXN_init )
#      Throw 2 rds, p1,p2 from unirnd()
#      Determine tau, u
#      update H
#      update S
#      update t_new= t+tau
#      Append S in File_name fomatted as [time \t,run #, spec # 1\t .... spec#6 /n]
#
#
# 

#include <stdio.h>              # This program simulates dynamics of affinity maturation in germinal centers 
import math
#include <time.h>	 	        # for seeding the rd # generator 
#include <limits.h>
#include "header_gillespie.h"
#include "MT19937-64.h"

#int main(void)
#{
#    int i
#    unsigned longinit = (0x12345ULL, 0x23456ULL, 0x34567ULL, 0x45678ULL), length=4
#    init_by_array64(init, length)
#    printf("1000 outputs of genrand64_int64()\n")
#    for (i=0; i<1000; i++) {
#      printf("%20llu ", genrand64_int64())
#      if (i%5==4) printf("\n")
#    }
#    printf("\n1000 outputs of genrand64_real2()\n")
#    for (i=0; i<1000; i++) {
#      printf("%10.8f ", genrand64_real2())
#      if (i%5==4) printf("\n")
#    }
#    return 0
#}

Gillespie_Fast(t_range, V_curr[Type_spe], C_curr, H_curr,S_curr[Type_dose], P_curr, f, num_RXN_curr,scheme) {


		t_new=0 # time marker for gillespie algorithm
		t_old= (double)t_range[0] # initialize time pt
		t_end= (double)t_range[1] # end point for gillespie algorithm # next rxn time #random # for reaction
		sum_prop= 0.0	#sum of propencities
#		unsigned int SEED
#random # draw from uniform distribution for next rxn time
		count=0
		unsigned longinit = (0x12345ULL, 0x23456ULL, 0x34567ULL, 0x45678ULL), length=4
		init_by_array64(init, length)
		# while t_new<t_end
        #printf("in function")
        #printf("%f",t_old)
        #printf("%f",t_end)
		while t_old<t_end:
                #printf("in loop")

				#Calc Propensity 
				Calc_H(S_curr,H_curr,scheme)

#/////////////////////////////////////////////////////////////////////////////////
#//					Validation
#					int i
#					for(i=0;i<num_RXN;i++){
#						printf("Gil_fast.H\n %e \n",H_curr[i])
#					}
#///////////////////////////////////////////////////////////////////////////////////
				Calc_P(H_curr,C_curr,P_curr)

#/////////////////////////////////////////////////////////////////////////////////
#//						Validation
#
#					for(i=0;i<num_RXN;i++){
#						printf("Gil_fast.P\n %e \n",P_curr[i])
#					}
#/////////////////////////////////////////////////////////////////////////////////

				sum_prop=Sum_P(P_curr, num_RXN_curr)
#/////////////////////////////////////////////////////////////////////////////////
#//						Validation
#				printf("Gil_fast.sumprop\n %e\n",sum_prop)
#/////////////////////////////////////////////////////////////////////////////////

				#Sample Tau: generate random number between (0,1) from MT twister
				random= genrand64_real3()
#				printf("%10.8f  ", genrand64_real3())

				if sum_prop > 0:
					tau = -logf(random)/sum_prop
					#printf("%f\n", sum_prop)
					#printf("%.17g\n", tau)
                    #printf("%10.35f\n", tau)
#/////////////////////////////////////////////////////////////////////////////////
#//						Validation
#						printf("Gil_fast.tau\n %e\n",tau)
#
#/////////////////////////////////////////////////////////////////////////////////

				else:
                        printf("%f\n" % (sum_prop))
						break

				#Select reaction 
				r= genrand64_real3()

#/////////////////////////////////////////////////////////////////////////////////
#//						Validation
#				printf("Gil_fast.rand\n %e\n",r)
#/////////////////////////////////////////////////////////////////////////////////
				reaction = select_reaction(P_curr, num_RXN_curr, sum_prop, r)
#/////////////////////////////////////////////////////////////////////////////////
#//						Validation
#				printf("Gil_fast.reaction\n %e\n",reaction)
#/////////////////////////////////////////////////////////////////////////////////

# temporary place to save it as buffer

				#update S 
				if count % 100000000 ==0:
				fprintf(f,"%.17g\t %f\t %f\t %f\t %f\t %f\t %f\n" % (t_old,S_curr[0][scheme],S_curr[1][scheme],S_curr[2][scheme],S_curr[3][scheme],S_curr[4][scheme],S_curr[5][scheme]))


	#			update_S(S_curr,V_curr,reaction,scheme)
					for(i=0; i<Type_spe; i++){
						S_curr[i][scheme] += V_curr[reaction][i]
#/////////////////////////////////////////////////////////////////////////////////
#//				Validation
#					for(i=0;i<Type_spe;i++){
#						printf("main_after_update.S\n %e \n",S_curr[i][scheme])
#					}
#/////////////////////////////////////////////////////////////////////////////////

				#Update t_new= t+tau 
#				printf("%.15f\n",tau)
#				printf("%.15f\n",t_old)
				t_new= t_old+tau
				t_old = t_new
				count = count+1
#				printf("%.15f\n",t_new)
#				printf("%.15f\n",t_end)

        printf("%f\n" % (sum_prop))



