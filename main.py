#
	# main.c
 # Created on: Oct 14, 2015
     # Author: Sunny K
     # Fast species evolution
     # Version 1. Without RXN 5, alpha=2
#
     	# Branch algorithm depending on the input_time range
     	# 1) t<=6
     	# for increment of the day
     	# Define v_s= v[1:2,:]
     	 	   # c_s= c[1:2,:]
     		   # H_s= Calc_H(S)[1:2,:]
    			# For each time domain
    				# Call [S]=Gillespie_Fast(time_range,v_s,c_s,H_s)
    				# Update S=S[0]+F(dose_type,day)
    				# Update H= Calc_H(S)
    		# 2) t>6
    		# Define V_s=V
    		 	   # C_s=C
    		 	   # H_s=H
    		 	   # Calc C_s(3)
    			# Call [S]=Gillespie_Fast(time_range,v_s,c_s,H_s)
				# Update H= Calc_H(S)
			# output Struct = [time \t,run #, spec # 1\t .... spec#6 /n]
			# Plot for each species
import sys
import numpy as np
from methods import init_F,init_V_C,Sum_P,update_S,select_reaction,Calc_H,Calc_P

# Define Parameters as globals, immutable
t	= 0.05	# total t span
Type_spe	= 6  # # of Type of species: C_Ag,C_B*,C_Ic,C_IgG,C_IgM,T_fH
Type_dose	= 4
num_RXN	= 5	# # of rxn
num_RXN_init	= 5 # # of rxn before t<6d
a	= 2			# Version 1 a=2
dose_per	= 1 # dosing period
Volume	= 0.000001 #volume of the lymph node, 1uL


def main():
	# /* rate constant matrix c */
	V=np.array([[-1,0,0,0,0,0],[-1,0,1,0,-1,0],[-1,0,1,-1,0,0],[0,-1,0,1,0,0],[0,0,0,0,0,a-1]])
	C= np.array([1,(8.64E7)/Volume,0,900,0])
	V_s= np.zeros((num_RXN,Type_spe),dtype=np.float)
	C_s= np.zeros(num_RXN,dtype=np.float)
	# /*Permutation matrix H  */
	H_s=np.zeros(num_RXN,dtype=np.float)
	# //Ag,B*,IC,IgG,IgM,Tfh
	S=[[0,0,0,0],[1E5,1E5,1E5,1E5],[0,0,0,0],[0,0,0,0],[1E13,1E13,1E13,1E13],[0,0,0,0]]  #/* state_matrix S: update once every */
	P=np.zeros(num_RXN,dtype=np.float) #/* propensity */
	F=np.zeros((dose_per,Type_dose),dtype=np.float)
	t_range =np.array([0,0],dtype=np.float)
	t_curr= 0.
	File_name= ['State_EI.txt','State_ED.txt','State_Const.txt','State_PB.txt'];

	for i in range(Type_dose):
		outputFiles[i] = open(File_name[i], "a+");
		print(File_name[i]);

	init_F(F)
	init_V_C(V_s,C_s,C,V)

	  #r1: Ag(0) decay, r2: IC(2) formation from IgM(4), r3:IC(2) formation from IgG(3), r4: IgG(3) prod, r5: Tfh(5) rep

#------------------ test set start-------------------------------------------------------------------- //

#	for (j=0;j<Type_dose;j++) /* Operate Gillespie for 1 day time domain*/
#		{
	i=0
	j=0

	Calc_H(S,H_s,j)

	outputFiles[j].write("time\tAg\tB\tIC\tIgM\tIgG\tTfh")
			# for t<= 6
		while i<dose_per:
			S[0,j]+= F[i,j] # Update S[0] by respective dosing by reading F

			print("main.S\n %10.3e\n" % (S[0,j]))
			Calc_H(S,H_s,j)
			t_range[0]=0
			t_range[1]=t
			print("6.1%f" % (t_range[1]))
			Gillespie_Fast(t_range,V_s,C_s,H_s,S,P,outputFiles[j],num_RXN_init,j) # UPdate S
			i=i+1


   State_EI.close()
   State_ED.close()
   State_Const.close()
   State_PB.close()

	   return 0
