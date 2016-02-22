

from . import _Dispatcher

class Dispatcher:


    def __init__(self):
        self._types = {} # func -> type
        self._children = {} # type -> disp
        self._sd = _Dispatcher()

    def register(self, f, _types):
        typ = _types[0]
        self._types[f] = typ
        self._sd.register(typ, f)
        cls = self.__class__

        if _types[1:]:
            d = self._children.setdefault(typ, cls())
            d.register(f, _types[1:])

    def dispatch(self, types):
        typ = types[0]
        types = types[1:]
        for match in self._sd.dispatch(typ):
            cls = self._types[match]
            child = self._children.get(cls)
            if not child:
                assert not types
                return match
            'fixme'
            if not types:
                continue
            ret = child.dispatch(types)
            if ret:
                return ret
        # return default
