from abc import ABCMeta


class Singleton(ABCMeta):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class A(metaclass=Singleton):
    pass

class B(metaclass=Singleton):
    pass

class C(B):
    pass

def test():
    a1 = A()
    a2 = A()

    b1 = B()
    b2 = B()

    c1 = C()
    c2 = C()

    assert a1 is a2, "Różne instancje"
    assert b1 is b2, "Różne instancje"
    assert c1 is c2, "Różne instancje"
    assert a1 is not b1, "Te same instancje"
    assert a1 is not c1, "Te same instancje"
    assert b1 is not c1, "Te same instancje"

if __name__ == "__main__":
    test()


