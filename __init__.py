

from .std import (
    get_cache_token, namedtuple, MappingProxyType,
    WeakKeyDictionary, update_wrapper, _c3_merge, _c3_mro,
    _compose_mro,
)

class _Dispatcher:
    '''
    Adapted `functools.singledispatch`
    '''

    #TODO dispatch_cache - list, not a value
    # finished: bool
    # or a generator, yielded: list

    def __init__(self):
        self.registry = {}

    def dispatch(self, cls):
        reg = self.registry.get(cls, ())
        yield from reg

        for impl in self._find_impl(cls):
            if reg and impl in reg:
                continue
            yield impl


    def register(self, cls, func):
        self.registry.setdefault(cls, []).append(func)
        # fixme dups ?

    def _find_impl(self, cls):
        #TODO make _compose_mro a generator
        registry = self.registry
        mro = _compose_mro(cls, registry.keys())
        match = None
        for t in mro:
            if match is not None:
                if (t in registry and t not in cls.__mro__
                                  and match not in cls.__mro__
                                  and not issubclass(match, t)):
                    raise RuntimeError("Ambiguous dispatch: {} or {}".format(
                        match, t))
                f = registry.get(match)
                if f:
                    yield from f
                continue
            if t in registry:
                match = t



def singledispatch(func):
    raise NotImplementedError("later")
