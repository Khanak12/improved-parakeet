class vehicle:
    def __init__(self,name, speed, milage):
        self.name=name
        self.speed=speed
        self.milage= milage
        
class bus(vehicle):
    pass
obj=bus("double decker bus",180, 12)
print(obj.name,obj.speed,obj.milage)


