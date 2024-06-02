import cv2
import numpy as np
import pyscreeze

SCREEN_SIZE = (1920, 1080)  # Разрешение экрана
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Кодек для видео
out = cv2.VideoWriter("output.avi", fourcc, 20.0, SCREEN_SIZE)  # Создание объекта записи видео

while True:
    screenshot = pyscreeze.screenshot()  # Сделать снимок экрана
    frame = np.array(screenshot)  # Преобразовать в массив NumPy
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Преобразовать цветовое пространство
    out.write(frame)  # Записать кадр в видео

    if cv2.waitKey(1) == ord("q"):  # Нажмите 'q', чтобы остановить запись
        break

out.release()  # Закрыть объект записи видео
cv2.destroyAllWindows()  # Закрыть окно