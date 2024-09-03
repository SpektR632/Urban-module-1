import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
            for participant in sorted(self.participants, key=lambda x: x.speed, reverse=True): 
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    all_results = None
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_1(self):
        run = Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = run.start()
        self.assertTrue(self.all_results[1][max(self.all_results[1])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_2(self):
        run = Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = run.start()
        self.assertTrue(self.all_results[2][max(self.all_results[2])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_3(self):
        run = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[3] = run.start()
        self.assertTrue(self.all_results[3][max(self.all_results[3])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_dop(self):
        run = Tournament(3, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[4] = run.start()
        self.assertTrue(self.all_results[4][max(self.all_results[4])] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            print(i)


if '__name__' == '__main__':
    unittest.main()
