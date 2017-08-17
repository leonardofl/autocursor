import win32api
from time import sleep

#Depende de pywin32 (https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/)

PASSO = 10
PAUSA_EM_SEGUNDOS = 0.8

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)

x = PASSO
y = PASSO
sentido_y = 1;
sentido_x = 0;
while True:

    win32api.SetCursorPos((x,y))
    x_antes, y_antes = x, y
    sleep(PAUSA_EM_SEGUNDOS)
    x, y = win32api.GetCursorPos()
    delta_x = x - x_antes
    delta_y = y - y_antes

    # detectando coice
    if abs(delta_x) > abs(delta_y):
        sentido_x = 1 if delta_x > 0 else -1
        sentido_y = 0
    if abs(delta_y) > abs(delta_x):
        sentido_y = 1 if delta_y > 0 else -1
        sentido_x = 0
    
    if sentido_y == 1:
        if y >= (height - PASSO):
            y = 0
            x = x + PASSO
        elif x >= (width - PASSO):
            x = 0

    if sentido_y == -1:
        if y <= PASSO:
            y = height
            x = x + PASSO
        elif x >= (width - PASSO):
            x = 0

    if sentido_x == 1:
        if x >= (width - PASSO):
            x = 0
            y = y + PASSO
        elif y >= (height - PASSO):
            y = 0

    if sentido_x == -1:
        if x <= PASSO:
            x = width
            y = y + PASSO
        elif y >= (height - PASSO):
            y = 0

    y = y + sentido_y * PASSO
    x = x + sentido_x * PASSO

