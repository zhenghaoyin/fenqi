def extra(func):
    def sing():
        print('sing')
        func()

    return sing


@extra
def speak():
    print("speak")


speak()


def ext():
    def sing():
        print('1')

    return sing


ex = ext()
ex()


class Danli(object):
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
            return cls._instance

        return cls._instance


d1 = Danli()
d2 = Danli()

print(d1)
print(d2)
