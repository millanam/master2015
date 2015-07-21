#ifndef matrix_f_h
#define matrix_f_h

extern void matrixsum_f(float *dest, const float *a, const float *b, unsigned int m, unsigned int n);

extern void matrixmul_f(float *dest, const float *a, const float *b, unsigned int m, unsigned int n, unsigned int p);

extern void matrixtrans_f(float *dest, const float *a, unsigned int m, unsigned int n);

#endif
