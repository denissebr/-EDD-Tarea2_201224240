import curses

class menu:
    def __init__(self, window):
        self.window = window

    def pintarmenu1(self):
        self.window.addstr(8, 16, "1 Mapeo por filas")
        self.window.addstr(9, 15, "2 Mapeo por columnas")
        self.window.addstr(10, 21, "3 Salir")

    def pedirdimensiones(self):
        self.window.addstr(8, 16, "Dimensiones: ")
        self.window.addstr(9, 20, "Enter Guardar")
        self.window.addstr(10, 20, "ESC Regresar")        
        self.window.addstr(19, 2, "Ejemplo de dimensiones: x,y")
        posx = posinicio = 29
        dimensiones = ""
        while True:
            event = self.window.getch()
            if event == 27:
                break
            else:
                if (event > 47 and event < 58) or event == 44:
                    #print(chr(event))
                    self.window.clear()
                    self.window.border(0)
                    self.window.addstr(8, 16, "Dimensiones: ")
                    self.window.addstr(9, 20, "Enter Guardar")
                    self.window.addstr(10, 20, "ESC Regresar")        
                    self.window.addstr(19, 2, "Ejemplo de dimensiones: x,y")
                    self.window.addstr(8, posinicio, dimensiones)
                    self.window.addstr(8, posx, chr(event))
                    posx += 1
                    dimensiones += chr(event)
                else:
                    if event == 8:
                        if posx != posinicio:
                            self.window.clear()
                            self.window.border(0)
                            self.window.addstr(8, 16, "Dimensiones: ")
                            self.window.addstr(9, 20, "Enter Guardar")
                            self.window.addstr(10, 20, "ESC Regresar")        
                            self.window.addstr(19, 2, "Ejemplo de dimensiones: x,y")
                            dimensiones = dimensiones[:-1]
                            self.window.addstr(8, posinicio, dimensiones)
                            posx -= 1
                    else:
                        if (event == 459 or event == 10) and posx != posinicio:
                            return dimensiones

    def pedirposicion(self):
        self.window.addstr(8, 16, "Posicion: ")
        self.window.addstr(9, 20, "Enter Guardar")
        self.window.addstr(10, 20, "ESC Regresar")        
        self.window.addstr(19, 2, "Ejemplo de posicion: x,y")
        posx = posinicio = 26
        dimensiones = ""
        while True:
            event = self.window.getch()
            if event == 27:
                break
            else:
                if (event > 47 and event < 58) or event == 44:
                    #print(chr(event))
                    self.window.clear()
                    self.window.border(0)
                    self.window.addstr(8, 16, "Posicion: ")
                    self.window.addstr(9, 20, "Enter Guardar")
                    self.window.addstr(10, 20, "ESC Regresar")        
                    self.window.addstr(19, 2, "Ejemplo de posicion: x,y")
                    self.window.addstr(8, posinicio, dimensiones)
                    self.window.addstr(8, posx, chr(event))
                    posx += 1
                    dimensiones += chr(event)
                else:
                    if event == 8:
                        if posx != posinicio:
                            self.window.clear()
                            self.window.border(0)
                            self.window.addstr(8, 16, "Posicion: ")
                            self.window.addstr(9, 20, "Enter Guardar")
                            self.window.addstr(10, 20, "ESC Regresar")        
                            self.window.addstr(19, 2, "Ejemplo de posicion: x,y")
                            dimensiones = dimensiones[:-1]
                            self.window.addstr(8, posinicio, dimensiones)
                            posx -= 1
                    else:
                        if (event == 459 or event == 10) and posx != posinicio:
                            return dimensiones

    def CalcularResultado(self, dimensiones, posiciones, tipo):
        auxdimensionx, auxdimensiony = dimensiones.split(",")
        auxposicionx, auxposiciony = posiciones.split(",")
        dimensionx = int(auxdimensionx)
        dimensiony = int(auxdimensiony)
        posicionx = int(auxposicionx)
        posiciony = int(auxposiciony)
        if dimensionx > posicionx and dimensiony > posiciony:
            if tipo == 49:
                resultado = posiciony * dimensionx + posicionx
                return resultado
            else:
                resultado = posicionx * dimensiony + posiciony
                return resultado
        else:
            return -1