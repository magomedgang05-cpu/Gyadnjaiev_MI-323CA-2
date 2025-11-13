products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}

max_sold_product = None
max_sold_count = 0

for product, info in products.items():
    if info["sold"] > max_sold_count:
        max_sold_count = info["sold"]
        max_sold_product = product

print(f"1. Самый продаваемый товар: {max_sold_product} ({max_sold_count} шт.)")

total_revenue = 0

for product, info in products.items():
    revenue = info["price"] * info["sold"]
    total_revenue += revenue

print(f"2. Общая выручка магазина: {total_revenue} руб.")

max_revenue_product = None
max_revenue = 0

for product, info in products.items():
    revenue = info["price"] * info["sold"]
    if revenue > max_revenue:
        max_revenue = revenue
        max_revenue_product = product

print(f"3. Товар с наибольшей выручкой: {max_revenue_product} ({max_revenue} руб.)")

print("\nДетали по всем товарам:")
for product, info in products.items():
    revenue = info["price"] * info["sold"]
    print(f"   {product}: цена {info['price']} руб., продано {info['sold']} шт., выручка {revenue} руб.")