'''
Define a mixin class from which two other classes inherit one common method and one common property.

Hints:

 1. A Mixin is a base class that contains methods for use by other classes without having to be the parent class of those other classes;
 1. Instead of using inheritance to distribute functionalities to different classes, you can use Mixins to package the functionality you want in one class, then inherit from that class wherever you want to use the functionality;
1. Essentially create a mixin class that two other classes inherit from.


 a Mixin is a base class that contains methods for use by other classes without having to be the parent class of those other classes. Instead of using inheritance to distribute functionalities to different classes, you can use Mixins to package the functionality you want in one class, then inherit from that class wherever you want to use the functionality
 
 '''

class Engine:
    
    '''
    The class Engine is the mixin class
    '''
    
    #  the @property decorator indicates a class property and is considered pythonic
    @property
    def eng_type(self):
        return "internal combustion engine"
    
    def move(self):
        print("Your vehicle moves")


# a second class to inherit a property and method from the mixin base class
class Car(Engine):
    pass

# a third class to inherit a property and method from the mixin base class
class Ship(Engine):
    pass


if __name__ == "__main__":
    # Instantiating classes from the second and third class 
    car = Car()
    ship = Ship()
    # printing the common property inherited from the mixin class
    print(car.eng_type)
    print(ship.eng_type)
    # running the common method inherited from the mixin class
    car.move()
    ship.move()