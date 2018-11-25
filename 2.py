class People(object):

    def __init__(self):
        self.v = 100

    # def __new__(cls, *args, **kwargs):
    #     print('123')

        # return cls

    @property
    def price(self):
        return self.v

    @price.setter
    def price(self, value):
        self.v = value


p = People()

print(p.price)
p.price = 200
print(p.price)
