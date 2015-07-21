#ifndef matrix_h
#define matrix_h

extern void matrixsum(int *dest, const int *a, const int *b, unsigned int m, unsigned int n);

extern void matrixmul(int *dest, const int *a, const int *b, unsigned int m, unsigned int n, unsigned int p);

extern void matrixtrans(int *dest, const int *a, unsigned int m, unsigned int n);

#endif
