

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
        try:
            from_reg = self.registry[cls]
            yield from_reg
        except KeyError:
            from_reg = None

        for impl in self._find_impl(cls):
            if from_reg and impl is from_reg:
                continue
            yield impl


    def register(self, cls, func):
        self.registry[cls] = func

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
                yield registry.get(match)
                continue
            if t in registry:
                match = t



def singledispatch(func):
    raise NotImplementedError("later")
