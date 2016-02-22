# from dispatch_2 import _Dispatcher



# def f(x):
#     assert isinstance(x, int)
#     return 'int'

# dis = _Dispatcher()
# dis.register(int, f)
# matches = dis.dispatch(int)
# print( list(matches))

def f(x, y):
    return x % y

def g(x, y):
    return x + y

def h(x, y, z):
    raise NotImplementedError


from .main import Dispatcher

class myint(int): pass

# import ipdb
# with ipdb.launch_ipdb_on_exception():
dis = Dispatcher()
dis.register(f, [str, int])
dis.register(g, [int, int])
dis.register(h, [str, int, int])
ret = dis.dispatch([str, myint])
'add test!'
print(ret)
