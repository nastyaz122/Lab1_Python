import tkinter as tk
from tkinter import simpledialog
from tkinter import colorchooser

line_thickness = 1
line_color = "black"

# Функция для рисования на холсте
def draw(event):
  x = event.x
  y = event.y
  # Создание овала с учётом выбранной толщины линии и цвета
  canvas.create_oval(x - line_thickness, y - line_thickness, x + line_thickness, y + line_thickness, fill=line_color, outline="")

# Функция для очистки холста
def clear_canvas():
  canvas.delete(tk.ALL)

# Функция для изменения толщины линии
def change_line_thickness():
    global line_thickness
    # Запрос новой толщины линии у пользователя
    new_thickness = simpledialog.askinteger("Выбор толщины линии", "Введите толщину линии:")
    if new_thickness is not None:
        line_thickness = new_thickness

# Функция для изменения цвета линии
def change_color():
  global line_color
  # Запрос нового цвета у пользователя
  color = colorchooser.askcolor(title="Выбор цвета")
  if color:
    line_color = color[1]

# Создание основного окна приложения
root = tk.Tk()
# Установка заголовка для основного окна
root.title("Лабораторная № 2")

# Создание холста (Canvas) размером 500x500 и добавление его на основное окно
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

main_menu = tk.Menu(root) 
# Настройка основного меню для основного окна
root.config(menu=main_menu) 

# Создание подменю "draw_menu" для основного меню
draw_menu = tk.Menu(main_menu)
main_menu.add_cascade(label="Меню", menu=draw_menu)
draw_menu.add_command(label="Очистить форму", command=clear_canvas) 
draw_menu.add_command(label="Выбрать толщину линии", command=change_line_thickness)
draw_menu.add_command(label="Выбрать цвет", command=change_color)

canvas.bind("<B1-Motion>", draw)  # Обработчик события для рисования при перемещении курсора с зажатой левой кнопкой мыши

root.mainloop()


