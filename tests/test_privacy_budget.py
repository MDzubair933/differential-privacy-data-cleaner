import unittest
from diffpriv.accountant import MomentsAccountant

class TestBudget(unittest.TestCase):
    def test_budget_accumulation(self):
        acc = MomentsAccountant()
        acc.step(0.01, 1.2)
        spent = acc.get_privacy_spent()
        self.assertTrue(spent['epsilon'] > 0)

if __name__ == '__main__':
    unittest.main()
