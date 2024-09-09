import unittest
import logging


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            obj = Runner('Вася', -5)
            logging.info(f"'test walk' выполнен успешно")
            for _ in range(10):
                obj.walk()
            self.assertEqual(obj.distance, 50)
        except Exception:
            logging.warning(f"Неверная скорость для Runner", exc_info=True)




    def test_run(self):
        try:
            obj = Runner(12)
            logging.info(f"'test run' выполнен успешно")
            for _ in range(10):
                obj.run()
            self.assertEqual(obj.distance, 100)
        except Exception:
            logging.warning(f"Неверный тип данных для объекта Runner", exc_info=True)




    def test_callenge(self):
        obj_1 = Runner('boy')
        for _ in range(10):
            obj_1.walk()

        obj_2 = Runner('men')
        for _ in range(10):
            obj_2.run()

        self.assertNotEqual(obj_1.distance, obj_2.distance)

if "__name__" == "__main__":

    logging.debug('Go')
    logging.info('Всё хорошо')
    logging.warning('НУ как же?')

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")


# first = Runner('Вася', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())