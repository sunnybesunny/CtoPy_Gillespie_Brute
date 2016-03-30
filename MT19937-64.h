/*
 * MT19937-64.h
 *
 *  Created on: Nov 11, 2015
 *      Author: User1
 */

#ifndef MT19937_64_H_
#define MT19937_64_H_

#define NN 312
#define MM 156
#define MATRIX_A 0xB5026F5AA96619E9ULL
#define UM 0xFFFFFFFF80000000ULL /* Most significant 33 bits */
#define LM 0x7FFFFFFFULL /* Least significant 31 bits */

void init_genrand64(unsigned long long seed);
void init_by_array64(unsigned long long init_key[],unsigned long long key_length);
unsigned long long genrand64_int64(void);
long long genrand64_int63(void);
double genrand64_real1(void);
double genrand64_real2(void);
double genrand64_real3(void);

#endif /* MT19937_64_H_ */
