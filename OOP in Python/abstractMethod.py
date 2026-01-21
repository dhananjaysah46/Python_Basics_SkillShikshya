from abc import ABC, abstractmethod
class demo(ABC):
    @abstractmethod
    def method1(self):
        print("This is abstract method 1")
        return
    def method2(self):
        print("This is concrete method 2")
class concreteDemo(demo):
    def method1(self):
        # super().method1()
        return

obj = concreteDemo()
obj.method1()
obj.method2()
# d = demo()  # This will raise an error because we cannot instantiate an abstract class

