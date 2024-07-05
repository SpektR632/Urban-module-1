class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        file = open(self.__file_name, 'a')
        file.close()

    def get_products(self):
        with open(self.__file_name) as file:
            return file.read()

    def add(self, *products):
        for product in products:
            if product.name not in self.get_products():
                with open(self.__file_name, 'a') as file:
                    file.write(product.__str__() + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


