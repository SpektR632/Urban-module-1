class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(*range(1, new_floor + 1), sep='\n')
        else:
            print('Такого этажа не существует')


object_1 = House('ЖК Эльбрус', 30)
object_1.go_to(31)
object_1.go_to(8)
