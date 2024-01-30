import tkinter as tk

class Matriz:
    def __init__(self, interface):
        # Ventana de la interfaz.
        self.interface = interface

        # Matriz que almacena los botones de la interfaz.
        self.buttons = [[None] * 5 for _ in range(10)]

        # Listas para buscar las columnas y filas desactivadas.
        self.disabled_columns = [False] * 5
        self.disabled_rows = [False] * 10

        # Crea los botones y los asigna a la matriz
        for i in range(10):
            for j in range(5):
                btn = tk.Button(interface, text=" ", width=5, height=2, command=lambda i=i, j=j: self.buttons_click(i, j))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn # Asigna el boton a la posicion correspondiente en la matriz

    def buttons_click(self, row, column):

        # Verificamos si la columna y la fila del boton seleccionado no estan desactivados.
        if not self.disabled_columns[column] and not self.disabled_rows[row]:

            # Recorre la fila, cambia el color de fondo y desactiva los botones
            for i in range(10):
                self.buttons[i][column].config(bg="red", state=tk.DISABLED)

            # Recorre la columna, cambia el color de fondo y desactiva los botones
            for j in range(5):
                self.buttons[row][j].config(bg="red", state=tk.DISABLED)

        # Marca la columna y fila como deshabilitadas
        self.disabled_columns[column] = True
        self.disabled_rows[row] = True


if __name__ == "__main__":
    interface = tk.Tk()
    app = Matriz(interface)
    interface.mainloop()
