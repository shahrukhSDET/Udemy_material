#METHOD RESOLUTION ORDER


class A:
    def say_hello(self):
        print("Hello from class A")

class B(A):
    def say_hello(self):
        print("Hello from class B")


class C(A):
    def say_hello(self):
        print("Hello from class A")

class D(B, C):
    pass

#In python, C3 Linearization algorithm is used to determine the MRO(METHOD RESOLUTION ORDER)
print(D.mro())

my_d = D()

my_d.say_hello()
