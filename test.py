class A():

    def __init__(self, name):
        self.name = name

    def read(self):
        text = input("type: ")
        print(text)
        return text

class B(A):

    def __int__(self, name):
        self.name = name


b = B("jojo")
b.read()
