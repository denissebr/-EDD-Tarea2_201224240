import curses
import pydot
import menu

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
            dimensionx, dimensiony = dimensiones.split(",")
            posicionx, posiciony = posiciones.split(",")
            resultado = menuta.CalcularResultado(dimensiones, posiciones, tecla)
            print(resultado)
            break

curses.endwin()