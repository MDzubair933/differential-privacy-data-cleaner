import math

class VectorClipper:
    def __init__(self, max_norm=1.0):
        self.max_norm = max_norm

    def clip_l2(self, vector):
        norm = math.sqrt(sum(x * x for x in vector))
        if norm > self.max_norm:
            scale = self.max_norm / (norm + 1e-9)
            return [x * scale for x in vector]
        return vector
