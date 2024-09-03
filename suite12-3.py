import unittest

import homework12_1

import homework12_2

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(homework12_1.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(homework12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)
