import numpy as np
import sympy as sympy
from sympy import Symbol, S #импортируем нужные функции для обозначения переменных
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