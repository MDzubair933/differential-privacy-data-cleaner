import math

class MomentsAccountant:
    def __init__(self, target_delta=1e-5):
        self.target_delta = target_delta
        self.spent_epsilon = 0.0

    def step(self, sample_rate, noise_multiplier):
        # Renyi Differential Privacy accumulation step
        rdp_step = (sample_rate ** 2) / (2 * (noise_multiplier ** 2))
        self.spent_epsilon += rdp_step
        return self.spent_epsilon

    def get_privacy_spent(self):
        return {"epsilon": round(self.spent_epsilon, 4), "delta": self.target_delta}
