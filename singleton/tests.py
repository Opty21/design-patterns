import inheritance
import threadLocal
import threadSafe
import cProfile

label = lambda text: f"\n======================== {text.upper()} ========================\n"

def localTest():
    print(label("Thread Local test"))
    return threadLocal.testSingleton()

def safeTest():
    print(label("Thread Safe test"))
    return threadSafe.testSingleton()

def inheritanceTest():
    print(label("Inheritance test"))
    return inheritance.test()

if __name__ == "__main__":
    cProfile.runctx('localTest()', globals(), locals())
    cProfile.runctx('safeTest()', globals(), locals())
    cProfile.runctx('inheritanceTest()', globals(), locals())
