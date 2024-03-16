from tkinter import *
from tkinter import ttk

def get_parametrs():
    parametrs.append(int(sizeX.get()))
    parametrs.append(int(sizeY.get()))
    parametrs.append(float(dif_coef.get()))
    parametrs.append(float(time_diffusion.get()))
    parametrs.append(float(step.get()))
    parametrs.append(float(t_step.get()))
    parametrs.append(float(vX.get()))
    parametrs.append(float(vY.get()))
    parametrs.append(int(radius.get()))
    parametrs.append(int(xSource.get()))
    parametrs.append(int(ySource.get()))
    parametrs.append(float(concentration.get()))
    parametrs.append(float(condition_up.get()))
    print(parametrs)
    root.destroy()  # Закрытие окна после передачи параметров

parametrs = []

root = Tk()     # создаем корневой объект - окно
root.title("Mathematic model")     # устанавливаем заголовок окна
root.geometry("500x400")    # устанавливаем размеры окна

label_main = ttk.Label(text="Основные параметры")
label_main.grid(row=0, column=0, columnspan=2)

label_sizeX = ttk.Label(text="Предельное значениее по оси X: ")
label_sizeX.grid(row=1, column=0, sticky=W)
sizeX = ttk.Entry()
sizeX.insert(0, 10)
sizeX.grid(row=1,column=1)

label_sizeY = ttk.Label(text="Предельное значениее по оси Y: ")
label_sizeY.grid(row=2,column=0, sticky=W)
sizeY = ttk.Entry()
sizeY.insert(0, 10)
sizeY.grid(row=2,column=1)

label_dif_coef = ttk.Label(text="Коэффициент диффузии: ")
label_dif_coef.grid(row=3,column=0, sticky=W)
dif_coef = ttk.Entry()
dif_coef.insert(0, 0.1)
dif_coef.grid(row=3,column=1)

label_time_diffusion = ttk.Label(text="Время протекания диффузии: ")
label_time_diffusion.grid(row=4,column=0, sticky=W)
time_diffusion = ttk.Entry()
time_diffusion.insert(0,3)
time_diffusion.grid(row=4,column=1)

label_step = ttk.Label(text="Шаг итерации: ")
label_step.grid(row=5,column=0, sticky=W)
step = ttk.Entry()
step.insert(0, 1)
step.grid(row=5,column=1)

label_t_step = ttk.Label(text="Шаг итерации по времени: ")
label_t_step.grid(row=6,column=0, sticky=W)
t_step = ttk.Entry()
t_step.insert(0, 0)
t_step.grid(row=6,column=1)

label_convection = ttk.Label(text="Параметры конвекции")
label_convection.grid(row=7, column=0, columnspan=2)

label_vX = ttk.Label(text="Скорость ветра по оси X: ")
label_vX.grid(row=8,column=0, sticky=W)
vX = ttk.Entry()
vX.insert(0, 0.1)
vX.grid(row=8,column=1)

label_vY = ttk.Label(text="Скорость ветра по оси Y: ")
label_vY.grid(row=9,column=0, sticky=W)
vY = ttk.Entry()
vY.insert(0, 0.1)
vY.grid(row=9,column=1)

label_source = ttk.Label(text="Параметры источника загрязнения")
label_source.grid(row=10, column=0, columnspan=2)

label_radius = ttk.Label(text="Радиус облака: ")
label_radius.grid(row=11, column=0, sticky=W)
radius = ttk.Entry()
radius.insert(0, 1)
radius.grid(row=11, column=1)

label_xSource = ttk.Label(text="Координаты центра источника по оси X: ")
label_xSource.grid(row=12, column=0, sticky=W)
xSource = ttk.Entry()
xSource.insert(0, 5)
xSource.grid(row=12,column=1)

label_ySource = ttk.Label(text="Координаты центра источника по оси Y: ")
label_ySource.grid(row=13, column=0, sticky=W)
ySource = ttk.Entry()
ySource.insert(0, 5)
ySource.grid(row=13,column=1)

label_concentration = ttk.Label(text="Количество загрязняющего вещества в точках источника: ")
label_concentration.grid(row=14,column=0, sticky=W)
concentration = ttk.Entry()
concentration.insert(0, 999)
concentration.grid(row=14,column=1)

chapter_condition_up = ttk.Label(text="Условие увеличения вещества в источнике")
chapter_condition_up.grid(row=15, column=0, columnspan=2)

label_condition_up = ttk.Label(text="Время продолжительности увеличения вещества в источнике")
label_condition_up.grid(row=16, column=0)
condition_up = ttk.Entry()
condition_up.insert(0, 0.5)
condition_up.grid(row=16,column=1)

btn = ttk.Button(text="Передать параметры", command = get_parametrs)
btn.grid(row=17, column=0, columnspan=2)
 
root.mainloop()
