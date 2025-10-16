from abc import ABC, abstractmethod

# ==============================
# STRATEGY PATTERN
# ==============================
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, order):
        pass

class WeightBasedStrategy(ShippingStrategy):
    def calculate(self, order):
        return order["weight"] * 5  # Exemplo: R$5 por kg

class DistanceBasedStrategy(ShippingStrategy):
    def calculate(self, order):
        return order["distance"] * 0.8  # Exemplo: R$0,80 por km

class FixedRateStrategy(ShippingStrategy):
    def calculate(self, order):
        return 20  # Taxa fixa

