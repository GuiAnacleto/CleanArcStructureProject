from dataclasses import dataclass
from datetime import date

@dataclass
class Sale:
    sale_id: int
    customer_id: int
    sale_date: date
    total_amount: float