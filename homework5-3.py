class Building:
    def __init__(self):
        self.numberOfFloors = 10
        self.buildingType = 'Магазин'
    def __eq__(self, other):
        return self.numberOfFloors == other.bnumberOfFloors and self.buildingType == other.buildingType

number_1 = Building()
number_2 = Building()
print(number_1.numberOfFloors == number_2.numberOfFloors)
print(number_1.buildingType == number_2.buildingType)
number_2.numberOfFloors, number_2.buildingType = 12, 'Музей'
print(number_1.numberOfFloors == number_2.numberOfFloors)
print(number_1.buildingType == number_2.buildingType)