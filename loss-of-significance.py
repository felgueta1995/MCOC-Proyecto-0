
import numpy as np
import scipy as sp
import matplotlib.pylab as plt

def error(real,calc):
    #Calcula error entre 2 numeros
    return abs( (calc-real) / real )

def promErrores(m1,m2):
    #Originalmente calculaba un arreglo de errores, y retornaba el promedio. 
    #Ahora retorna el maximo error dentro de un arreglo
    n=m1.shape[0]
    a=np.zeros(n*n,dtype=sp.float64)
    c=0
    for i in range(n):
        for j in range(n):
            if (i==j):
                a[c]=error(m1[i,j],m2[i,j])
                c+=1
    #return sp.mean(a,dtype=sp.float64)
    return np.amax(a)


#A continuacion, los codigos para crear las matrices de Hillbert 
#con dimension n*n; de tipos de datos sp.float32 y sp.float64
def Hillbert32(n):
    m=np.zeros((n,n),dtype=sp.float32)
    for i in range (1,n+1):
        for j in range(1,n+1):
            m[i-1,j-1]=1.0/(i+j-1)
    return np.mat(m)

def Hillbert64(n):
    m=np.zeros((n,n),dtype=sp.float64)
    for i in range (1,n+1):
        for j in range(1,n+1):
            m[i-1,j-1]=1.0/(i+j-1)
    return np.mat(m)


#A continuacion creo una lista de n's para los que calculare el error
enes=range(2,100)

errors32  = np.zeros(len(enes),dtype=sp.float64)
errors64  = np.zeros(len(enes),dtype=sp.float64)

for i in enes:

    #Aqui calculare el error en la diagonal de la matriz identidad y la matiz H(n)*H(n)^-1 (Supuesta Identidad)

    Identity=np.eye(i)

    m32=Hillbert32(i)
    Im32=m32.I
    I=Im32.dot(m32)
    errors32[i-enes[0]]=promErrores(Identity,I)

    m64=Hillbert64(i)
    Im64=m64.I
    I=Im64.dot(m64)
    errors64[i-enes[0]]=promErrores(Identity,I)


#Plot relative errors
plt.figure(1)

plt.semilogy(enes, errors32, label="matriz con dtype=sp.float32")
plt.semilogy(enes, errors64, label="matriz con dtype=sp.float64")

plt.xlabel("$N$")
plt.ylabel("Error relativo")

plt.grid(True)

#Set the legend to be outside the ax
ax = plt.gca()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, 0.81*box.height])
ax.legend(loc='lower left', bbox_to_anchor=(0, 1.00))

plt.savefig("loss-of-significance.png")

plt.show()
    