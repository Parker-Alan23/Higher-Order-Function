def add(a):
    def func(b):
        return a + b
    return func
twoMore = add(2)
x = 10
xPlusTwo = twoMore(x)
print(xPlusTwo)
