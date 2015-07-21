CC=gcc

ifeq ($(PRODUCTION),1)
    CFLAGS=-O3 -std=c99
else
    CFLAGS=-g -std=c99
endif


default: matrix_f.so

matrix_f.so: matrix_transf_f.c matrix_oper_f.c
	${CC} ${CFLAGS} -o matrix_f.so -shared matrix_transf_f.c matrix_oper_f.c

matrix_transf_f.o: matrix_transf_f.c
	${CC} ${CFLAGS} -o matrix_transf_f.o -c matrix_transf_f.c

matrix_oper_f.o: matrix_oper_f.c
	${CC} ${CFLAGS} -o matrix_oper_f.o -c matrix_oper_f.c

clean:
	rm matrix_oper_f.o matrix_transf_f.o matrix_f.so 
