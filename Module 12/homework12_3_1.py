import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        obj = Runner('boy')
        for _ in range(10):
            obj.walk()

        self.assertEqual(obj.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj = Runner('men')
        for _ in range(10):
            obj.run()

        self.assertEqual(obj.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_callenge(self):
        obj_1 = Runner('boy')
        for _ in range(10):
            obj_1.walk()

        obj_2 = Runner('men')
        for _ in range(10):
            obj_2.run()

        self.assertNotEqual(obj_1.distance, obj_2.distance)
