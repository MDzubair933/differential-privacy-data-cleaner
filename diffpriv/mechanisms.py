import math
import random

class DifferentialPrivacyEngine:
    def __init__(self, epsilon=1.0, delta=1e-5):
        self.epsilon = epsilon
        self.delta = delta

    def laplace_noise(self, scale):
        u = random.random() - 0.5
        return -scale * math.copysign(1.0, u) * math.log(1.0 - 2.0 * abs(u))

    def perturb_numeric(self, true_val, sensitivity=1.0):
        scale = sensitivity / self.epsilon
        noise = self.laplace_noise(scale)
        return true_val + noise
