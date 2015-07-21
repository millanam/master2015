CC=gcc

ifeq ($(PRODUCTION),1)
    CFLAGS=-O3 -std=c99
else
    CFLAGS=-g -std=c99
endif


default: matrix.so

matrix.so: matrix_transf.c matrix_oper.c
	${CC} ${CFLAGS} -o matrix.so -shared matrix_transf.c matrix_oper.c

matrix_transf.o: matrix_transf.c
	${CC} ${CFLAGS} -o matrix_transf.o -c matrix_transf.c

matrix_oper.o: matrix_oper.c
	${CC} ${CFLAGS} -o matrix_oper.o -c matrix_oper.c

clean:
	rm matrix_oper.o matrix_transf.o matrix.so 
