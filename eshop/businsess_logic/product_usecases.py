from typing import Optional, List

from eshop.businsess_logic.product import Product
from eshop.data_access.product_repo import save, get_by_id, get_many


def product_create(id: str, name: str, price: float):
        save(
            Product(
                id=id,
                name=name,
                price=price,
            ))



def product_get_by_id(id: str) -> Optional[Product]:
   return get_by_id(id)


def product_get_many() -> List[Product]:
    return get_many()
