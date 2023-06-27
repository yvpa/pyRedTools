
class _Wrapper:

    def __init__(self, cls):
        self.__wrapped__ = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.__wrapped__(*args, **kwargs)
        return self._instance


def singleton(cls):
    return _Wrapper(cls)
