import pydot
import os

class graficar:
    def __init__(self, dimensionx, dimensiony, posicionx, posiciony):
        self.posicionx = posicionx
        self.posiciony = posiciony
        self.dimensionx = dimensionx
        self.dimensiony = dimensiony
    
    def creargrafica(self):
        posx = 0
        posy = 0
        grafica = "digraph{\n"
        grafica += str("node[shape=record];\n")
        grafica += str("rankdir = LR;\n")
        for fil in range(self.dimensiony):
            for col in range(self.dimensionx):
                if fil == self.posiciony and col == self.posicionx:
                    grafica += str("nodo" + str(fil) + "_" + str(col) + "[style=\"filled\" label=\"(" + str(fil) + "," + str(col) + ")\" pos=\"" + str(posx) + "," + str(posy) + "!\" fillcolor=\"#ff7f0e\"];\n")
                else:    
                    grafica += str("nodo" + str(fil) + "_" + str(col) + "[label=\"(" + str(fil) + "," + str(col) + ")\" pos=\"" + str(posx) + "," + str(posy) + "!\"];\n")
                posx += 1
            posx = 0
            posy -= 1
        grafica += str("}")
        print(grafica)
        archivo = open("archivo.dot", "w+")
        archivo.write(grafica)
        archivo.close()
        os.system("neato -Tjpg archivo.dot -o salida.jpg")