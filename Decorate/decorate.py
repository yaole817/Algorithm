def log(func):
    def wrapper(*args, **kwargs):
        print("call %s():" % func.__name__)
        return func(*args, **kwargs)
    return wrapper


def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

def newLog(text):
    if callable(text):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print("%s %s():" % (text, func.__name__))
                return func(*args, **kwargs)
    else:
        def wrapper(*args, **kwargs):
            print("call %s():" % func.__name__)
            return func(*args, **kwargs)

@newLog("excute")
def newNow(a,b):
    print('2017-9-8')
    print(a,b)

@log("excute")
def now(a,b):
    print('2017-9-8')
    print(a,b)


if __name__ == "__main__":
    newNow(7,'h')