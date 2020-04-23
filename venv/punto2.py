from itertools import combinations
import math
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def main():

    x = []
    y = []
    z = []
    ninos = []
    nin = 0
    combina = []
    cadenas = []
    f_cadena = []
    p_f= []
    dt= 0
    d_t=[]
    #numero de rutas
    n = int(input())
    fig = plt.figure()
    grafica = fig.add_subplot(111, projection='3d')
    for j in range(n):
        r = int(input())

        for k in range(r):
            punto = input()
            tmpa = punto.split(" ")
            x.append(int(tmpa[0]))
            y.append(int(tmpa[1]))
            z.append(int(tmpa[2]))
            ninos.append(int(tmpa[3]))
            nin = nin + int(tmpa[3])
            combina.append(k+1)
            print(combina)
        p_f.append(nin)
        nin = 0
        a = list(combinations(combina, 2))
        for p in a:
            q = calculo_dist(x, y, z, p)
            tmp = q.split(" ")
            dt = dt + float(tmp[2])
            cadenas.append(q)
        d_t.append(dt)
        dt = 0
        # --------------------------------------
        # Creamos la figura

        # Agrrgamos un plano 3D

        #grafica.plot_wireframe(np.array([x]),np.array([y]), np.array([z]))
        grafica.plot(x, y, z, marker='o', c=np.random.rand(3,),label = f"Ruta {j+1} \n distancia: {d_t[j]} \n niños cazados {p_f[j]}")

        grafica.set_title("Rutas")
        grafica.set_xlabel('eje x')
        grafica.set_ylabel('eje y')
        grafica.set_zlabel('eje z')
        plt.legend(loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5),fontsize = 'xx-small',framealpha=0.4)

        if n < 3 :

            zdirs = (None, 'x', 'y', 'z', (1, 1, 0), (1, 1, 1))


            for zdir, x, y, z in zip(zdirs, x, y, z):
                label = '(%d, %d, %d), dir=%s' % (x, y, z, zdir)
                grafica.text(x, y, z, label, zdir)



        # --------------------------------------
        x = []
        y = []
        z = []
        f_cadena.append(cadenas)
        cadenas = []
        combina = []
    plt.show()
    for m in range(len(p_f)):
        print(f"La distancia de la ruta {m+1} es de {d_t[m]} se cazaron {p_f[m]} niños ")


def calculo_dist(x, y ,z,p):
    global cadenas
    dist = math.sqrt(math.pow(x[p[0]-1]-x[p[1]-1],2) + math.pow(y[p[0]-1]-y[p[1]-1],2) + math.pow(z[p[0]-1]-z[p[1]-1],2))
    #print(dist)
    cadena = f"{p[0]} {p[1]} {round(dist,3)}"

    #print(cadena)
    return cadena


if __name__ == "__main__":
    main()

