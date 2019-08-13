import pydot
import os

class graficar:
    def __init__(self, dimensionx, dimensiony, posicionx, posiciony):
        self.posicionx = posicionx
        self.posiciony = posiciony
        self.dimensionx = dimensionx
        self.dimensiony = dimensiony
    
    def creargrafica(self, tipo):
        posx = 0
        posy = -1
        grafica = "digraph{\n"
        grafica += str("subgraph cluster_matriz{\n")
        grafica += str("subgraph cluster_dib{\n")
        grafica += str("node[shape=box];\n")
        for fil in range(self.dimensiony):
            for col in range(self.dimensionx):
                if fil == self.posiciony and col == self.posicionx:
                    grafica += str("nodo" + str(fil) + "_" + str(col) + "[style=\"filled\" label=\"(" + str(fil) + "," + str(col) + ")\" pos=\"" + str(posx) + "," + str(posy) + "!\" fillcolor=\"#ff7f0e\"];\n")
                else:    
                    grafica += str("nodo" + str(fil) + "_" + str(col) + "[label=\"(" + str(fil) + "," + str(col) + ")\" pos=\"" + str(posx) + "," + str(posy) + "!\"];\n")
                posx += 1
            posx = 0
            posy -= 1
        grafica += str("}\n}\n")
        grafica += str("subgraph clusterlinealizacion{\n")
        if tipo == 49:
            for fil in range(self.dimensiony):
                for col in range(self.dimensionx):
                    if fil == self.posiciony and col == self.posicionx:
                        grafica += str("lineal" + str(fil) + "_" + str(col) + "[style=\"filled\" label=\"(" + str(fil) + "," + str(col) + ")\" pos=\"" + str(posx) + "," + str(posy) + "!\" fillcolor=\"#ff7f0e\"];\n")
                    else:
                        grafica += str("lineal" + str(fil) + "_" + str(col) + "[label=\"(" + str(fil) + "," + str(col) + ")\" pos=\"" + str(posx) + "," + str(posy) + "!\"];\n")
                    posx += 1
        else:
            for col in range(self.dimensionx):
                for fil in range(self.dimensiony):
                    if fil == self.posiciony and col == self.posicionx:
                        grafica += str("lineal" + str(fil) + "_" + str(col) + "[style=\"filled\" label=\"(" + str(fil) + "," + str(col) + ")\" pos=\"" + str(posx) + "," + str(posy) + "!\" fillcolor=\"#ff7f0e\"];\n")
                    else:
                        grafica += str("lineal" + str(fil) + "_" + str(col) + "[label=\"(" + str(fil) + "," + str(col) + ")\" pos=\"" + str(posx) + "," + str(posy) + "!\"];\n")
                    posy -= 1
        
        grafica += str("}\n}")
        print(grafica)
        archivo = open("archivo.dot", "w+")
        archivo.write(grafica)
        archivo.close()
        os.system("neato -Tjpg archivo.dot -o salida.jpg")