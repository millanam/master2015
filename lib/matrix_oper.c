#include "matrix.h"

void matrixsum(int *dest, const int *a, const int *b, unsigned int m, unsigned int n) {
	for (unsigned int i = 0; i < m; i++) {
		for (unsigned int j = 0; j < n; j++) {
			dest[i*n+j] = a[i*n+j] + b[i*n+j];
		}
	}
}


void matrixmul(int *dest, const int *a, const int *b, unsigned int m, unsigned int n, unsigned int p) {
	for (unsigned int i = 0; i < m; i++) {
		for (unsigned int j = 0; j < p; j++) {
			int sum = 0;
			for (unsigned int k = 0; k < n; k++) {
				sum += a[i*n+k] * b[k*p+j];
			}
			dest[i*p+j] = sum;
		}
	}
}
