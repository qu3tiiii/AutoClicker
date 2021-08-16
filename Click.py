#Hola, ahora te enseñare a crear un "auto clicker" en 5 lineas de codigo!
#Primero importamos lo necesario
import pyautogui, time
#El tiempo de espera para empezar los clicks
time.sleep(3)
#La cantidad de clicks
for x in range(10):
    pyautogui.click()
    pass
