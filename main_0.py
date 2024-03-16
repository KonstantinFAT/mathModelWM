import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import GUI_MM

# Создайте главное окно tkinter
root = tk.Tk()
root.title("Моя анимация графика")

# Создайте Frame для размещения холста с графиком
frame = tk.Frame(root)
frame.pack()

# Создайте холст для отображения графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack()

# Помещение облака в поле
grid = np.zeros((GUI_MM.parametrs[0], GUI_MM.parametrs[1], 10))
for i, plane in enumerate(grid):
    for j, line in enumerate(plane):
        for k, column in enumerate(line):
            if ((GUI_MM.parametrs[9] - GUI_MM.parametrs[8] <= i <= GUI_MM.parametrs[9] + GUI_MM.parametrs[8]) and
                    (GUI_MM.parametrs[10] - GUI_MM.parametrs[8] <= j <= GUI_MM.parametrs[10] + GUI_MM.parametrs[8]) and
                    (5 - GUI_MM.parametrs[8] <= k <= 5 + GUI_MM.parametrs[8])):
                grid[i, j, k] = GUI_MM.parametrs[11]
                
# Создание трехмерной сетки
x = np.arange(0, GUI_MM.parametrs[0], 1)
y = np.arange(0, GUI_MM.parametrs[1], 1)
z = np.arange(0, 10, 1)
x, y, z = np.meshgrid(x, y, z)



# Диффузия
def update(frame):
    ax.clear()
    plt.title(f"График протекания диффузии - время {round(frame * 0.1)} sec")
    ax.scatter(x, y, z, c=grid.flatten(), cmap='viridis')
    for i in range(1, GUI_MM.parametrs[0] - 1):
        for j in range(1, GUI_MM.parametrs[1] - 1):
            for k in range(1, 9):
                grid[i, j, k] = grid[i, j, k] + GUI_MM.parametrs[2] * (
                    GUI_MM.parametrs[6] * (grid[i + 1, j, k] - grid[i - 1, j, k]) / GUI_MM.parametrs[4] +
                    (grid[i + 1, j, k] - 2 * grid[i, j, k] + grid[i - 1, j, k]) / GUI_MM.parametrs[4] +
                    GUI_MM.parametrs[7] * (grid[i, j + 1, k] - grid[i, j - 1, k]) / GUI_MM.parametrs[4] +
                    (grid[i, j + 1, k] - 2 * grid[i, j, k] + grid[i, j - 1, k]) / GUI_MM.parametrs[4] +
                    0.1 * (grid[i, j, k + 1] - grid[i, j, k - 1]) / GUI_MM.parametrs[4] +
                    (grid[i, j, k + 1] - 2 * grid[i, j, k] + grid[i, j, k - 1]) / GUI_MM.parametrs[4])
    return grid

# Создание анимации
ani = animation.FuncAnimation(fig, update, frames=int(GUI_MM.parametrs[3] / 0.1), interval=200, repeat=False)

# Запустить главный цикл tkinter
root.mainloop()
