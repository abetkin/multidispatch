from dispatch_2 import _Dispatcher



def f(x):
    assert isinstance(x, int)
    return 'int'

dis = _Dispatcher()
dis.register(int, f)
matches = dis.dispatch(int)
print( list(matches))
