from abc import ABC
from shipping_strategy import DistanceBasedStrategy, FixedRateStrategy, ShippingStrategy, WeightBasedStrategy

# ==============================
# SHIPPING COMPANY (Contexto da Strategy)
# ==============================
class ShippingCompany(ABC):
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ShippingStrategy):
        """Permite trocar a estratégia em tempo de execução."""
        self.strategy = strategy

    def calculate_shipping(self, order):
        return self.strategy.calculate(order)


class CorreiosSedex(ShippingCompany):
    def __init__(self):
        super().__init__(WeightBasedStrategy())


class TransportadoraXYZ(ShippingCompany):
    def __init__(self):
        super().__init__(DistanceBasedStrategy())


class RetiradaNaLoja(ShippingCompany):
    def __init__(self):
        super().__init__(FixedRateStrategy())
