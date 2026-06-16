# # # import test
# # from test import *
# #
# # ardager = Hero('Ardager')
# #
# # print(ardager.name)
# # print(add(12, 12))
# # print(random.randint(1, 10))
#
#
#
# from my_package import Hero, add_test, add
# # import  random
# # import  sqlite3
#
#
#
# print("TEXT")yle

# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

import random
from tenacity import retry


@retry
def do_something_unreliable():
    if random.randint(0, 10) > 1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"


print(do_something_unreliable())