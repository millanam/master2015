#include "matrix_f.h"

void matrixtrans_f(float *dest, const float *a, unsigned int m, unsigned int n) {
	for (unsigned int i = 0; i < m; i++) {
		for (unsigned int j = 0; j < n; j++) {
			dest[j*m+i] = a[i*n+j];
		}
	}
}
