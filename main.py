class vehicle:
  def __init__(self,name,max_speed,mileage):
    self.max_speed=max_speed
    self.mileage=mileage
    self.name=name


    def display_info(self):
      return f"vehicle name: {self.name}\n max speed: {self.max_speed}\n mileage: {self.mileage}"
    
      
class bus(vehicle):
    def __init__(self,name,max_speed,mileage,capacity):
        super().__init__(name,max_speed,mileage)
        self.capacity=capacity
    
    def display_info(self):
        return f"vehicle name: {self.name}\n max speed: {self.max_speed}\n mileage: {self.mileage}"

school_bus=bus("volvo",150,12000,50)
print(school_bus.display_info())
# The code defines a class hierarchy for vehicles, with a base class `vehicle` and a derived class `bus`.
# The `vehicle` class has attributes for name, max speed, and mileage, and a method to display this information.
# The `bus` class inherits from `vehicle` and adds a capacity attribute.
# An instance of the `bus` class is created and its information is displayed using the `display_info` method.
# The output will show the name, max speed, and mileage of the bus.
# The code defines a class hierarchy for vehicles, with a base class `vehicle` and a derived class `bus`.       


