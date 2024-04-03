from abc import ABC, abstractmethod

class food(ABC):
    @abstractmethod
    def taste(self):
        pass

class pizza(food):

    def taste(self):
        print('pizza taste')

    def size(self):
        print('12-inch pizza')

#=====================================================

p = pizza()
p.size()


class A(ABC):
    @abstractmethod
    def method1(self):
        pass

#=====================================================

class B(A):

    @abstractmethod
    def method2(self):
        pass

#=====================================================
    
class C(B):

    def method1(self):
        print("method1 is overridden")

    def method2(self):
        print('method2 is overridden')

b = C()

b.method1()
b.method2()
        
