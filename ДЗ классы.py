'''12. Реализовать класс вектор (произвольной размерности), у которого должны быть
методы сложения с другим вектором, и умножения на число, а также скалярного
произведения с другим вектором. Кроме того должен быть метод, возвращающей
длину вектора. Реализуйте корректный вывод вектора с помощью функции print.'''
from math import sqrt

class Vector:
    def __init__(self, x, y): #Пусть пространство будет двумерным
        self.x=x
        self.y=y
    
    def x(self):
        return self.x    #Задаём значения аргумента х класса свойствам объекта(вектора)
        
    def y(self):
        return self.y    #Задаём значения аргумента y класса свойствам объекта(вектора)
 
    def __str__(self):      #Если надо вывести координаты вектора
        return "("+str(self.x)+","+str(self.y)+")"
 
    def __add__(self, other):  #Сумма векторов - получаем координаты вектора
        return (self.x+other.x,self.y+other.y)
        
    def __sub__(self, other):   #Разность векторов - получаем координаты вектора
        return (self.x-other.x,self.y-other.y)
        
    def __mul__(self, other):   #Скалярное произведение векторов
        return self.x*other.x+self.y*other.y
        
    def __rmul__(self,k):      #Умножение вектора на скаляр
        return Vector(k*self.x,k*self.y)

    def _length_(self):          #Длина вектора
        return sqrt((self.y)*(self.y)+(self.x)*(self.x))

        
v1=Vector(12,4)    #Проверка и вывод
v2=Vector(10,-2)     
print('Сумма векторов: ',v1+v2)
print('Координаты: ',v2)
print('Скалярное v1*v2: ',v1*v2)
print('Длина вектора: ',v1._length_())    
print('Умножение вектора на 5: ',v2.__rmul__(5))

            
 
