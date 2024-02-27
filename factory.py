
# Design Pattern :: Factory
# 팩토리 패턴은 객체 생성과정을 간편화하고, 이 단계를 클라이언트 코드로부터 분리하는데에 주 목적이 있다.

# Factory Method
# 객체 생성을 위한 인터페이스를 정의하고, 구체적인 사항은 서브클래스에서 정하는것.
# 즉, Factory Method 패턴을 이용하여, 클래스의 인스턴스를 만드는 일을 서브클래스에게 맡긴다.
from abc import ABCMeta, abstractmethod


# interface walk를 정의하고, 구체적인 구현은 Anima을 상속받는 서브클래스에게 위임한다.
# abstractmethod를 적용하여, 강제성을 부여.
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

    @classmethod
    def createAnimal(cls):
        return cls()


# subclass에서 walk를 구체적으로 구현.
class Dog(Animal):
    def walk(self):
        print('Dog is walking...')


# client에서 Factory Method를 사용하는 모습.
def createAnimal(type):
    if type == 'dog':
        return Dog.createAnimal()


# Abstract Factory Method
# Factory Method를 생성하는 중간단계를 한단계 더 생성함으로써,
# 의존하는 객체를 생성할 수 있음.
class Button(metaclass=ABCMeta):
    @abstractmethod
    def click(self):
        pass


# Factory Method
class WindowsButton(Button):
    def click(self):
        print('windows button click.')


# 중간단계에 Abstract Factory Method를 추가.
class GUIFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_button(self):
        pass


# 해당 Abstract Factory Method에서 정의한 create_button을 정의한다.
# 이렇게 함으로써, Factory Method에서 정의한 class를 생성할때, 추가 연관된 작업들을 할 수 있다.
# 여기선 Window Button을 생성할때 mouse icon을 전에 넣고 싶어서 이런식으로 구현할 수 있다.
class WindowsFactory(GUIFactory):
    def create_button(self):
        print('move mouse icon')
        return WindowsButton()

# application에서 Abstract Factory Method를 이용하는 모습.
def application(factory_type):
    if factory_type == "windows":
        factory = WindowsFactory()
    return factory.create_button()


application('windows')
