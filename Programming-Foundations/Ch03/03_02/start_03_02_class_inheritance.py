""" A Garage Full of Classy Vehicles """

class Vehicle: # Base Vehicle class
    
    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4 # a full tank of gas
    
    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print('The {} {} goes VROOOM!'.format(self.color, self.manuf))
        else:
            print('The {} {} sputters out of gas.'.format(self.color, self.manuf))
            
class Car(Vehicle): # Inherits from Vehicle class
    
    # turn the radio on
    def radio(self):    
        print("Rockin' Tunes!")

    # open the window
    def window(self):
        print('Ahhh... fresh air!')
            
class Motorcycle(Vehicle): # Inherits from Vehicle class
    
    # put on motocycle helmet
    def helmet(self):
        print('Nice and safe!')

class ECar(Car):
    def drive(self):
        print('The {} {} goes shhhhhhhh...' .format(self.color, self.manuf))

my_ecar = ECar('white', 'Nissan')
my_ecar.radio()
my_ecar.window()
my_ecar.drive()
print(my_ecar.gas)

""" My Experiments with overriding methods """

class eCar(Car):
    Car.power = 4
    
    def drive(self):
        if self.gas > 0:
            self.gas = 0
        if self.power > 0:
            self.power -= 1
            print('The {} {} goes shhhhhhhh...' .format(self.color, self.manuf))
        else:
            print('The {} {} comes to a quiet stop.' .format(self.color, self.manuf))

my_eCar = eCar('white', 'Nissan')
my_eCar.radio()
my_eCar.window()
my_eCar.drive()
print(my_eCar.gas)
print(my_eCar.power)
