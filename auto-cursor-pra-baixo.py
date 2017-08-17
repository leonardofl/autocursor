import win32api
from time import sleep

#Depende de pywin32 (https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/)

PASSO = 10
PAUSA_EM_SEGUNDOS = 0.8

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)

x = PASSO
y = PASSO
while True:
    win32api.SetCursorPos((x,y))
    sleep(PAUSA_EM_SEGUNDOS)
    x, y = win32api.GetCursorPos()
    if y >= (height - PASSO):
        y = 0
        x = x + PASSO
    elif x >= (width - PASSO):
        x = 0
    y = y + PASSO
