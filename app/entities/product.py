from dataclasses import dataclass

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int