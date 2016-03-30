/*
 * 	main.c
 *  Created on: Oct 14, 2015
 *      Author: Sunny K
 *      Fast species evolution
 *      Version 1. Without RXN 5, alpha=2
 *
 *      	Branch algorithm depending on the input_time range
 *      	1) t<=6
 *      	for increment of the day
 *      	Define v_s= v[1:2,:]
 *      	 	   c_s= c[1:2,:]
 *      		   H_s= Calc_H(S)[1:2,:]
 *     			For each time domain
 *     				Call [S]=Gillespie_Fast(time_range,v_s,c_s,H_s)
 *     				Update S=S[0]+F(dose_type,day)
 *     				Update H= Calc_H(S)
 *     		2) t>6
 *     		Define V_s=V
 *     		 	   C_s=C
 *     		 	   H_s=H
 *     		 	   Calc C_s(3)
 *     			Call [S]=Gillespie_Fast(time_range,v_s,c_s,H_s)
 *				Update H= Calc_H(S)
*			output Struct = [time \t,run #, spec # 1\t .... spec#6 /n]
*			Plot for each species
 */
#include <stdio.h>              /* File I/O */
//#include <stdlib.h>
#include <math.h>               /* for logf*/
//#include <time.h>	 	        /* for seeding the rd # generator */
#include "header_gillespie.h"
#include <limits.h>

FILE *State_EI;
FILE *State_ED;
FILE *State_Const;
FILE *State_PB;

int main(void){


	int i,j;
	  //r1: Ag(0) decay, r2: IC(2) formation from IgM(4), r3:IC(2) formation from IgG(3), r4: IgG(3) prod, r5: Tfh(5) rep
	double V[num_RXN][Type_spe]= {{-1,0,0,0,0,0},{-1,0,1,0,-1,0},{-1,0,1,-1,0,0},{0,-1,0,1,0,0},{0,0,0,0,0,a-1}}; /*stoichiometry matrix */
	double C[num_RXN]= {1,(8.64E7)/Volume,0,900,0};      /* rate constant matrix c */
	double V_s[num_RXN][Type_spe]={{0.}};
	double C_s[num_RXN]= {0.};
	double H_s[num_RXN]= {0.}; /*Permutation matrix H  */
	//Ag,B*,IC,IgG,IgM,Tfh
	double S[Type_spe][Type_dose]={{0,0,0,0},{1E5,1E5,1E5,1E5},{0,0,0,0},{0,0,0,0},{1E13,1E13,1E13,1E13},{0,0,0,0}};  /* state_matrix S: update once every */
	//double S[Type_spe][Type_dose]={{0.}};  /* state_matrix S: update once every */
	double P[num_RXN]={0.}; /* propensity */
	double F[dose_per][Type_dose]={{0.}};
	double	t_range[1]={0};
	double t_curr= 0.;
	char * File_name[]= {"State_EI.txt","State_ED.txt","State_Const.txt","State_PB.txt"};

	for (i = 0; i < Type_dose; i++)
	{
		outputFiles[i] = fopen(File_name[i], "a+");
	    printf("%s\n",File_name[i]);
	}

//	/*Open up dosing schedule file, state files  */
//	State_EI=fopen("State_EI.txt", "w");
//	State_ED=fopen("State_ED.txt", "a+");
//	State_Const=fopen("State_Const.txt", "a+");
//	State_PB=fopen("State_PB.txt", "a+");


	/*Initialize F*/
	init_F(F);

	/* initialize V_s,C_s,H_s  */
	init_V_C(V_s,C_s,C,V);

//------------------ test set start-------------------------------------------------------------------- //

//	for (j=0;j<Type_dose;j++) /* Operate Gillespie for 1 day time domain*/
//		{
	i=0;
	j=0;

	Calc_H(S,H_s,j);

	fprintf(outputFiles[j],"%s\t %s\t %s\t %s\t %s\t %s\t %s\n","time","Ag","B","IC","IgM","IgG","Tfh");

			/* for t<= 6 */
		while(i<dose_per)
			{
			S[0][j]+= F[i][j]; /* Update S[0] by respective dosing by reading F*/

			printf("main.S\n %e\n",S[0][j]);
			Calc_H(S,H_s,j);
			t_range[0]=0;
			t_range[1]=t;
			printf("%f",t_range[1]);
			Gillespie_Fast(t_range,V_s,C_s,H_s,S,P,outputFiles[j],num_RXN_init,j); /* UPdate S*/
			i=i+1;
			}
//			t_curr= dose_per;

			/* for t> 6 */
//				while(t_curr<= t[1])
//					{
//						Calc_H(*S,*H_s); /* Update H_s from update S */
//						Calc_C_s(*C_s);
//						t_range[0]=0; /*should be relevant time point*/
//						t_range[1]=1; /*should be relevant time point*/
//						Gillespie_Fast(*t_range,*V_s,*C_s,*H_s,*S,*P,File_name[j],num_RXN);
//						t_curr= t_range[1];
//					}
//		}

//------------------ test set end--------------------------------------------------------------------- //


//	original code
//
//		for (j=0;j<Type_dose;j++) /* Operate Gillespie for 1 day time domain*/
//			{
//			Calc_H(S,H_s,j);
//
//				/* for t<= 6 */
//				for(i=0;i<dose_per;i++)
//					{
//						S[0][j]+= F[i][j]; /* Update S[0] by respective dosing by reading F*/
//						Calc_H(S,H_s,j);
//						t_range[0]=i;
//						t_range[1]=i+1;
//						Gillespie_Fast(*t_range,V_s,C_s,H_s,S,P,File_name[j],num_RXN_init,j); /* UPdate S*/
//					}
//				t_curr= dose_per;
//
//				/* for t> 6 */
////				while(t_curr<= t[1])
////					{
////						Calc_H(*S,*H_s); /* Update H_s from update S */
////						Calc_C_s(*C_s);
////						t_range[0]=0; /*should be relevant time point*/
////						t_range[1]=1; /*should be relevant time point*/
////						Gillespie_Fast(*t_range,*V_s,*C_s,*H_s,*S,*P,File_name[j],num_RXN);
////						t_curr= t_range[1];
////					}
//			}


   fclose(State_EI);
   fclose(State_ED);
   fclose(State_Const);
   fclose(State_PB);

	   return (0);
}
