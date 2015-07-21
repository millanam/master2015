import sys
import ctypes

#Funcion para imprimir matriz
def printmatrix(X, m, n):
	print(m, n)
	for i in range(0, m):
		print(' '.join(str(x) for x in X[i*n:i*n+n]))

#Cargando la librería compartida
libmatrix = ctypes.CDLL("./matrix.so")

#Comprobamos parametros
if len(sys.argv) < 3:
	print("Faltan parametros")
	sys.exit()

size = []
operacion = sys.argv[1]

#Leemos la primera matriz
file1 = sys.argv[2]
f1 = open(file1)
for sizeline in f1.readline().strip().split():
		size.append(int(sizeline))
A = []
for line in f1.read().strip():
	for number in line.split():
		A.append(int(number))
c_A = (ctypes.c_int * len(A))(*A)
f1.close()

if operacion == "Trans":
	############################
	# Transpuesta de una matriz
	############################
	
	#Realizamos la operacion transpuesta
	R = [0] * size[1] * size[0]
	c_R = (ctypes.c_int * len(R))(*R)
	libmatrix.matrixtrans(ctypes.byref(c_R), ctypes.byref(c_A), ctypes.c_uint(size[0]), ctypes.c_uint(size[1]));
	R = [c_R[i] for i in range(size[1] * size[0])]
	
	#Imprimimos el resultado
	printmatrix(R,size[1],size[0])
	
elif operacion == "Sum":
	############################
	# Suma de matrices
	############################
	
	if len(sys.argv) < 4:
		print("Faltan parametros")
		sys.exit()
	
	#Leemos la segunda matriz
	file2 = sys.argv[3]
	f2 = open(file2)
	for sizeline in f2.readline().strip().split():
		size.append(int(sizeline))
	B = []
	for line in f2.read().strip():
		for number in line.split():
			B.append(int(number))
	c_B = (ctypes.c_int * len(B))(*B)
	f2.close()
	
	if size[0] != size[2] and size[1] != size[3]:
		print("Las matrices tienen distintos tamaños, no se pueden sumar")
		sys.exit()
	
	#Realizamos la operacion de suma
	R = [0] * size[0] * size[1]
	c_R = (ctypes.c_int * len(R))(*R)
	libmatrix.matrixsum(ctypes.byref(c_R), ctypes.byref(c_A), ctypes.byref(c_B), ctypes.c_uint(size[0]), ctypes.c_uint(size[1]));
	R = [c_R[i] for i in range(size[0] * size[1])]
	
	#Imprimimos el resultado
	printmatrix(R,size[0],size[1])
	
elif operacion == "Mult":
	############################
	# Multiplicacion de matrices
	############################
	
	if len(sys.argv) < 4:
		print("Faltan parametros")
		sys.exit()
	
	#Leemos la segunda matriz
	file2 = sys.argv[3]
	f2 = open(file2)
	for sizeline in f2.readline().strip().split():
		size.append(int(sizeline))
	B = []
	for line in f2.read().strip():
		for number in line.split():
			B.append(int(number))
	c_B = (ctypes.c_int * len(B))(*B)
	f2.close()
	
	if size[1] != size[2]:
		print("El número de columnas de la primera matriz no es el mismo que el numero de filas de la segunda matriz, no se pueden multiplicar")
		sys.exit()
	
	R = [0] * size[0] * size[3]
	c_R = (ctypes.c_int * len(R))(*R)
	libmatrix.matrixmul(ctypes.byref(c_R), ctypes.byref(c_A), ctypes.byref(c_B), ctypes.c_uint(size[0]), ctypes.c_uint(size[1]), ctypes.c_uint(size[3]));
	R = [c_R[i] for i in range(size[0] * size[3])]
	
	#Imprimimos el resultado
	printmatrix(R,size[0],size[3])
	
else:
	print("Operacion no reconocida")
	sys.exit()
