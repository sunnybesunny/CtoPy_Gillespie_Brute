import numpy as np

def init_F(F_curr):

	with open('F_dosing_schedule.txt','r') as f:
		F_curr=[x.strip().split('\t') for x in f]

	print F_curr
	return F_curr

def init_V_C(C_ref,V_ref):
	C_curr= C_ref
	V_curr= V_ref #Why oh why???
	return C_curr,V_curr

def Sum_P(P,num_RXN_curr):
	sum_prop=0
	for i in range(num_RXN_curr):
			sum_prop = sum_prop+P[i]

	return sum_prop
def update_S(S_curr, V_curr,reaction, scheme):

	S_curr[:,scheme] += V_curr[reaction,:]
	return S_curr

def select_reaction(P, num_RXN_curr, sum_propencity, randN):
	reaction = -1
	sp = 0.0
	randN = randN * sum_propencity
	for(i=0; i<num_RXN_curr; i++):
		sp += P[i]
		#printf("sp: %f\n", sp)
		if randN < sp:
	    #printf("randN: %f\n",randN)
			reaction = i
			break
	return reaction

def Calc_H(S_curr, H_curr,j):
	H_curr[0] = S_curr[0,j]
	H_curr[1] =S_curr[4,j]*S_curr[0,j]
	H_curr[2] =S_curr[3,j]*S_curr[0,j]
	H_curr[3] =S_curr[1,j]
	H_curr[4] =S_curr[5,j]
	return H_curr
	
def Calc_P( H_curr,C_curr, P_curr):
	P_curr=  H_curr*C_curr
	return P_curr
