
import math
import sys
import numpy as np
from methods import init_F,init_V_C,Sum_P,update_S,select_reaction,Calc_H,Calc_P
import random

# generate rd float between (0,1]
def rand_gen():
    floatinfo = numpy.finfo(float)
    epsilon = floatinfo.eps
    a = np.random.uniform(0+eps, 1+eps)
    return a

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
# This program simulates dynamics of affinity maturation in germinal centers

def Gillespie_Fast(t_range, V_curr, C_curr, H_curr,S_curr, P_curr, f, num_RXN_curr,scheme):

	t_new=0 # time marker for gillespie algorithm
	t_old= float(t_range[0]) # initialize time pt
	t_end= floar(t_range[1]) # end point for gillespie algorithm # next rxn time #random # for reaction
	sum_prop= 0.0	#sum of propencities
	#		unsigned int SEED
	#random # draw from uniform distribution for next rxn time
	count=0

	while t_old<t_end:
	        #printf("in loop")
			#Calc Propensity
		Calc_H(S_curr,H_curr,scheme)

	#/////////////////////////////////////////////////////////////////////////////////
	#//					Validation
	#						print H_curr
	#
	#///////////////////////////////////////////////////////////////////////////////////
		Calc_P(H_curr,C_curr,P_curr)

	#/////////////////////////////////////////////////////////////////////////////////
	#//						Validation
	#
	#						print P_curr
	#
	#/////////////////////////////////////////////////////////////////////////////////
		sum_prop=Sum_P(P_curr, num_RXN_curr)
	#/////////////////////////////////////////////////////////////////////////////////
	#//						Validation
	#				print sum_prop
	#/////////////////////////////////////////////////////////////////////////////////

					#Sample Tau: generate random number between (0,1) from MT twister
		random= rand_gen()
	#				print random

		if sum_prop > 0:
			tau = -np.log(random)/sum_prop
						#printf("%f\n", sum_prop)
						#printf("%.17g\n", tau)
	                    #printf("%10.35f\n", tau)
	#/////////////////////////////////////////////////////////////////////////////////
	#//						Validation
	#						printf("Gil_fast.tau\n %e\n",tau)
	#
	#/////////////////////////////////////////////////////////////////////////////////

		else:
	            print sum_prop
				break

		#Select reaction
		r= rand_gen()
#/////////////////////////////////////////////////////////////////////////////////
#//						Validation
#				print ("Gil_fast.rand\n %10.3e\n" %(r))
#/////////////////////////////////////////////////////////////////////////////////
		reaction = select_reaction(P_curr, num_RXN_curr, sum_prop, r)
#/////////////////////////////////////////////////////////////////////////////////
#//						Validation
#				print("Gil_fast.reaction\n %10.3e\n"%(reaction))
#/////////////////////////////////////////////////////////////////////////////////

# temporary place to save it as buffer

				#update S
	if (count % 100000000 ==0):
	State_str = ("%10.3e\t%10.3e\t%10.3e\t%10.3e\t%10.3e\t%10.3e\t%10.3e\n" % (t_old,S_curr[0,scheme],S_curr[1,scheme],S_curr[2,scheme],S_curr[3,scheme],S_curr[4,scheme],S_curr[5,scheme]))
	f.write(State_str)

	#			update_S(S_curr,V_curr,reaction,scheme)
	for i in range(Type_spe):
		S_curr[i,scheme] += V_curr[reaction,:].T
#/////////////////////////////////////////////////////////////////////////////////
#//				Validation
#						print S_curr
#					}
#/////////////////////////////////////////////////////////////////////////////////
				#Update t_new= t+tau
#				print tau
#				print t_old
	t_new= t_old+tau
	t_old = t_new
	count = count+1
#				print t_new
#				print t_end

    print  sum_prop
