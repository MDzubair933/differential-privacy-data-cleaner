from .mechanisms import DifferentialPrivacyEngine

class TabularSynthesizer:
    def __init__(self, epsilon=1.0):
        self.dp = DifferentialPrivacyEngine(epsilon=epsilon)

    def synthesize_column(self, values):
        return [self.dp.perturb_numeric(v) for v in values]
