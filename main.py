import datetime
import random

class Timer:

    def __init__(self, user_message = None):

        self.user_message = user_message

    def __enter__(self):
        self.t_start = datetime.datetime.now()
        print('Выполнение кода в менеджере контекста')
        print(self.user_message)

    def __exit__(self, exc_type, exc_value, traceback):
        self.t_stop = datetime.datetime.now()
        self.t_delta = self.t_stop - self.t_start
        print(f'Начало выполнения программы: {self.t_start}\nКонец выполнения программы: {self.t_stop}\nВремя выполнения программы: {self.t_delta}\n')


def get_me_pi(pixel, radius): #Вычисление числа Пи методом Монте-Карло
    
    summ = 0

    for count in range(pixel):

        x_axe  = random.randint(0, radius)
        y_axe  = random.randint(0, radius)

        if x_axe ** 2 + y_axe ** 2 < radius ** 2:
            summ += 1

    return summ / count * 4

pi = 3.1415926535897932
      
#pixel = 1000000
radius = 10000

pix_gen = [10 ** i for i in range(1, 7)]

for pixel in pix_gen:
    with Timer(f'Количество точек: {pixel}'):
        print(f'Вычисленное число Пи: {get_me_pi(pixel, radius)}\nПогрешность: {get_me_pi(pixel, radius) - pi}')




