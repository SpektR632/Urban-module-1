class House:
    def __init__(self):
        self.numberOfFloors = 0
    
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


obj = House()
print(obj.numberOfFloors)
obj.setNewNumberOfFloors(6)
