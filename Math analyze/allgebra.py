import numpy as np
import sympy as sympy
from sympy import * #импортируем нужные функции для обозначения переменных
from sympy.calculus.util import function_range #импортируем функцию для поиска области значения
from sympy.calculus.util import continuous_domain #импортируем функцию для поиска области определения
x = Symbol("x") #определяем нашу переменную
f = 1/x #определяем нашу функцию
print(continuous_domain(f, x, S.Reals)) #вычисляем область определения
from sympy import log
x = Symbol("x")
f = log(x)/x
print(continuous_domain(f, x, S.Reals))
''' aeyrwbz'''
from sympy import sin
x = Symbol("x")
f = sin(x)
print(function_range(f, x, S.Reals))

from sympy import exp #добавляем функцию для вычисления экспоненциальной функции
x = Symbol("x")
f = (x*x-3)/(exp(x))
print(function_range(f, x, S.Reals))

x = Symbol("x")
f = x**2 + 2*x -8
print(f.subs(x, 0))

from sympy import solveset, Eq
print(solveset(Eq(x**2 + 2*x -8, 0), x))
x = Symbol("x")
f = x**2 + 2*x -8
print(f.subs(x, 0))

from sympy import solveset, Eq
print(solveset(Eq(x**2 + 2*x -8, 0), x))

from sympy import diff
x = Symbol("x")
f = x**4 + 5*x
print(f.diff(x,2))

#Область определения
x = Symbol("x")
f = (x**3)/(x**2 - 1)
print(continuous_domain(f, x, S.Reals)) #Область определения функции f от x, S.Reals - вещественные числа

#Область значений функции
f = (x**3)/(x**2 - 1)
print(function_range(f, x, S.Reals))

#Нахождение точек пересечения с осями координат
f = (x**3)/(x**2 - 1)
print(solveset(Eq(f,0), x)) # 
print(f.subs(x, 0)) # 

# Нахождение производной
f = (x**3)/(x**2 - 1)
print(f.diff(x)) # 

y = f.diff(x)
print(solveset(Eq(y, 0), x)) # 

from sympy import exp #добавляем функцию для вычисления экспоненциальной функции
x = Symbol("x")
f = 1/(1+(exp(x)**(-4)))
print(function_range(f, x, S.Reals))
print(f)

from sympy import symbols, cos, diff

a, b, c = symbols('a b c', real=True)
f = 5*a*b - a*cos(c) + a**8 + c**2*b

print(diff(f, a))

