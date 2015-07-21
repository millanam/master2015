#include "matrix_f.h"

void matrixsum_f(float *dest, const float *a, const float *b, unsigned int m, unsigned int n) {
	for (unsigned int i = 0; i < m; i++) {
		for (unsigned int j = 0; j < n; j++) {
			dest[i*n+j] = a[i*n+j] + b[i*n+j];
		}
	}
}


void matrixmul_f(float *dest, const float *a, const float *b, unsigned int m, unsigned int n, unsigned int p) {
	for (unsigned int i = 0; i < m; i++) {
		for (unsigned int j = 0; j < p; j++) {
			float sum = 0;
			for (unsigned int k = 0; k < n; k++) {
				sum += a[i*n+k] * b[k*p+j];
			}
			dest[i*p+j] = sum;
		}
	}
}
