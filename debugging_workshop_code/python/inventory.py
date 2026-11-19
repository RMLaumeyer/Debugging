def reserve_inventory(products, order):
    for item in order["items"]:
        product = next((p for p in products if p["id"] == item["product_id"]), None)
        if product is not None and product["stock"] >= item["quantity"]: # no stock amount check
            product["stock"] -= item['quantity'] # Corrected stock deductions


def restock_product(products, product_id, amount):
    if amount < 1 and not isinstance(amount, int): 
        return None
    for product in products:
        if product["id"] == product_id:
            product["stock"] += amount
            return product
    return None
