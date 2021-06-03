# Напишете програма, която чете ъгъл в радиани (rad) и го преобразува в градуси (deg). Принтирайте
# получените градуси като цяло число използвайки math.floor.
# Използвайте формулата: градуси = радиани * 180 / π. Числото π в Python може да достъпите чрез модула
# math. За да ползвате функционалността му, първо трябва да включите констатата pi.
#
# Aко използвате първия вариант, в програмата ви методът ще бъде достъпен посредством кода math.pi, ако
# използвате втория – само pi. Може да упражните и двата варианта.
# Важно: Библиотеката math ни предоставя константи и статични методи за тригонометрични, логаритмични и
# други общи математически функции. Повече информация може да прочетете от тук.

from math import pi
from math import floor

rad = float(input())
deg = rad * 180/pi
print(floor(deg))
