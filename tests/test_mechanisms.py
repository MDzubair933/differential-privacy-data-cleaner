import unittest
from diffpriv.mechanisms import DifferentialPrivacyEngine

class TestMechanisms(unittest.TestCase):
    def test_laplace_perturbation(self):
        engine = DifferentialPrivacyEngine(epsilon=1.0)
        perturbed = engine.perturb_numeric(100.0)
        self.assertNotEqual(perturbed, 100.0)
        self.assertTrue(abs(perturbed - 100.0) < 50.0)

if __name__ == '__main__':
    unittest.main()
