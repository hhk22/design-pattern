
# Design Pattern :: Factory
# 클래스의 인스턴스를 만드는 일을 서브클래스에게 맡기는 것.

# Factory Method
# 단일 객체 생성에 초점.
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class Dog(Animal):
    def walk(self):
        print('dog is walking...')


class Cat(Animal):
    def walk(self):
        print('cat is walking...')


class AnimalFactory:
    def createAnimal(self, animal: str):
        if animal == "dog":
            return Dog()
        elif animal == "cat":
            return Cat()


animal_factory = AnimalFactory()
dog = animal_factory.createAnimal('dog')
dog.walk()

# Abstract Factory Method
# 관련된 객체의 서브그룹들을 생성하는데 초점.
class AFMAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def rest(self):
        pass

    @abstractmethod
    def run(self):
        pass


class AFMDog(Animal):
    def walk(self):
        print('dog is warlking...')

    def rest(self):
        print('dog is resting...')

    def run(self):
        print('dog is running')


class AFMCat(Animal):
    def walk(self):
        print('cat is warlking...')

    def rest(self):
        print('cat is resting...')

    def run(self):
        print('cat is running')


# Factory 패턴으로 생성된 class 들의 서브동작으로 구성된 메소드.
# Factory Method 방식 자체는 단일 객체의 구현에 집중했다면
# Abstract Factory Method 방식은 서브 그룹의 동작을 한데로 모은것에 초점을 둔다.
def application():
    dog = AFMDog()
    cat = AFMCat()

    dog.walk()
    cat.walk()

    dog.rest()

    dog.run()
    cat.run()


application()
