import my_package.main_func

from my_package.main_operations import *

import my_package.file_operations

y = my_package.main_func.x2(4)
print(y)

z = plus(1,3,5)
print(z)

sp = my_package.file_operations.open_file('sp.txt')
print(sp)