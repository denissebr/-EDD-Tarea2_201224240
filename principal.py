import curses
import pydot
import menu
import graficar

curses.initscr()
window = curses.newwin(20, 50, 0, 0)
window.timeout(300)
window.keypad(True)
curses.noecho()
curses.curs_set(0)
window.border(0)
menuta = menu.menu(window)
menuta.pintarmenu1()

while True:
    tecla = window.getch()
    if tecla == 51:
        break
    else:
        if tecla == 49 or tecla == 50:
            window.clear()
            window.border(0)
            dimensiones = menuta.pedirdimensiones()
            window.clear()
            window.border(0)
            posiciones = menuta.pedirposicion()
            print(dimensiones)
            print(posiciones)
            if dimensiones and posiciones:
                dimensionx, dimensiony = dimensiones.split(",")
                posicionx, posiciony = posiciones.split(",")
                resultado = menuta.CalcularResultado(dimensiones, posiciones, tecla)
                print(resultado)
                window.clear()
                window.border(0)
                if resultado == -1:
                    window.addstr(9, 12, "Las posiciones ingresadas")
                    window.addstr(10, 10, "fueron mayor a las dimensiones")
                    window.addstr(11, 11, "1 Regresar al menu principal")
                    tecla1 = -1
                    while tecla1 != 49:
                        tecla1 = window.getch()
                    window.clear()
                    window.border(0)
                    menuta.pintarmenu1()
                else:
                    window .addstr(10, 20, "Resultado {}".format(resultado))
                    window.addstr(11, 11, "1 Regresar al menu principal")
                    gra = graficar.graficar(int(dimensionx), int(dimensiony), int(posicionx), int(posiciony))
                    gra.creargrafica(tecla)
                    tecla1 = -1
                    while tecla1 != 49:
                        tecla1 = window.getch()
                    window.clear()
                    window.border(0)
                    menuta.pintarmenu1()
            else:
                window.clear()
                window.border(0)
                menuta.pintarmenu1()
curses.endwin()