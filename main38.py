class bird:
    def __init__(self):
        print("print bird is ready")
    
    def func1(self):
        print("I am from the parent")
        
    def swim(self):
        print("swim faster")
    
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin")
        
obj=penguin()
obj.func1()
