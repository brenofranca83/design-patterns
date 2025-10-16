from shipping_factory import ShippingFactory
from shipping_strategy import FixedRateStrategy

# ==============================
# CÓDIGO CLIENTE 
# ==============================

if __name__ == "__main__":
    # Simulação de pedido
    order = {
        "weight": 3.5,     # kg
        "distance": 120,   # km
    }

    # Método de envio escolhido
    shipping_type = "sedex"  

    company = ShippingFactory.get_shipping_company(shipping_type)

    cost = company.calculate_shipping(order)
    print(f"Custo do frete ({shipping_type}): R$ {cost:.2f}")

    # --- Demonstração do recurso extra: trocar Strategy em runtime ---
    print("Trocando estratégia para taxa fixa...")
    company.set_strategy(FixedRateStrategy())
    print(f"Novo custo do frete: R$ {company.calculate_shipping(order):.2f}")
