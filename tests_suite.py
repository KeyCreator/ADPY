import unittest
from tests import test_app, test_api, test_selenium

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests1 = loader.loadTestsFromModule(test_app)
    tests2 = loader.loadTestsFromModule(test_api)
    tests3 = loader.loadTestsFromModule(test_selenium)
    suite.addTests(tests1)
    suite.addTests(tests2)
    suite.addTests(tests3)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
