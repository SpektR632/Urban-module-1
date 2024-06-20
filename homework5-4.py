class Building:
    total = 0
    def __init__(self):
        self.name = 'Барак'
        self.total = Building.total
        Building.total += 1

for i in range(40):
    print(Building().__dict__)
print(Building.total)