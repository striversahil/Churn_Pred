from abc import ABC , abstractmethod


# Abstract Class
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete Class
class Circle(Shape):
    def draw(self):
        return 'You Choosed Circle'
    
# Concrete Class
class Rectangle(Shape):
    def draw(self):
        return 'You Choosed Rectangle'
    


class ShapeFactory:
    def getShape(self , shapeType):
        if shapeType == 'Circle':
            return Circle().draw()
        elif shapeType == 'Rectangle':
            return Rectangle().draw()
        else:
            return None
        

if __name__ == '__main__':
    factory = ShapeFactory()
    print(factory.getShape('Circle'))
    print(factory.getShape('Rectangle'))




