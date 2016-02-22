
from functools import singledispatch

import abc

class typ(abc.ABC):
    1

class typ2(abc.ABC):
    1


typ.register(int)
typ2.register(int)


@singledispatch
def fun(x):
    raise NotImplementedError


@fun.register(typ)
def plus1(x):
    return x + 1



# @fun.register(int)
# def iden(x):
#     return x


class myint(int): pass


print( fun( myint(3)))
