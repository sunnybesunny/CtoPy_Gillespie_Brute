/*
 * header_gillespie.h
 *
 *  Created on: Oct 20, 2015
 *      Author: Sunny K
 *        Pseudocode:
 *      	Define 		time span t=[0,40] (day)
 *      	Define 		Type-dose
 *      	Define 		Num RXN
 *      	Define 		Num RXN-init
 *      	Define 		a Tfh expansion factor
 *      	Define 		dose per
 *      	Define 		Ag_dosing Matrix,F(dose_type,day)
 *      	Define 		stoichiometric matrix v
 *      	Initialize 	species #
 *      	Initialize	rate constant matrix c,
 *      				Permutation matrix h
 *      	Initialize 	state_matrix S[type_spe][type_dose]
 *
 *			RXN:
 *			1. C_Ag --> 0
 *			2. C_IgM+C_Ag-->C_Ic
 *			3. C_IgG+C_Ag-->C_Ic
 *			4. C_B*-->C_IgG
 *			5. T_fh-->aT_fh (V1. a=2)
 */

#ifndef HEADER_GILLESPIE_H
#define HEADER_GILLESPIE_H

#include <stdio.h>              /* This program simulates dynamics of affinity maturation in germinal centers */
//#include <stdlib.h>


#define Sqr(a) (a)*(a)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))


/* Define Parameters as macros*/
#define t 0.05	/* total t span */
#define Type_spe 6  /* # of Type of species: C_Ag,C_B*,C_Ic,C_IgG,C_IgM,T_fH */
#define Type_dose 4
#define num_RXN 5	/* # of rxn*/
#define num_RXN_init 5 /* # of rxn before t<6d*/
#define a 2			/* Version 1 a=2*/
#define dose_per 1 /* dosing period*/
#define Volume 0.000001 /*volume of the lymph node, 1uL  */

/* Variables */
extern double V[num_RXN][Type_spe]; /*stoichiometry matrix */
extern double C[num_RXN] ;   /* rate constant matrix c */
extern double V_s[num_RXN][Type_spe];
extern double C_s[num_RXN];
extern double H_s[num_RXN]; /*Permutation matrix H  */
extern double S[Type_spe][Type_dose];  /* state_matrix S: need to be dynamically allocated, maybe not*/
extern double P[num_RXN]; /* propensity */
extern float F[dose_per][Type_dose];
extern double t_range[1];
extern double t_curr;
extern char * File_name[Type_dose];
FILE *outputFiles[Type_dose-1];

/*function prototypes*/
void init_F(double[dose_per][Type_dose]);
void Calc_H(double[Type_spe][Type_dose], double[num_RXN ],int);
void init_V_C(double[num_RXN][Type_spe], double[num_RXN],double[num_RXN],double[num_RXN][Type_spe]);
void Calc_P(double[num_RXN], double[num_RXN], double[num_RXN]);
double Sum_P(double[num_RXN],int);
int select_reaction(double[num_RXN], int, double, double);
void update_S(double[Type_spe][Type_dose], double[num_RXN][Type_spe],int,int);
void Gillespie_Fast(double [1], double[num_RXN][Type_spe], double[num_RXN], double[num_RXN],double[Type_spe][Type_dose], double[num_RXN], FILE *, int, int);

#endif /* HEADER_GILLESPIE_H_ */
