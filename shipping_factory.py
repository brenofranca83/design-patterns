from shipping_company import CorreiosSedex, RetiradaNaLoja, ShippingCompany, TransportadoraXYZ

# ==============================
# FACTORY METHOD
# ==============================

class ShippingFactory:
    @staticmethod
    def get_shipping_company(method: str) -> ShippingCompany:
        method = method.lower()
        if method == "sedex":
            return CorreiosSedex()
        elif method == "xyz":
            return TransportadoraXYZ()
        elif method == "retirada":
            return RetiradaNaLoja()
        else:
            raise ValueError(f"Método de envio desconhecido: {method}")

