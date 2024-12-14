discount = 0
discount_price = 0
def fuel_price(litres, price_per_litre):
    if litres % 2 == 0:
        discount = litres / 2 * 5
    else:
        discount = (litres - 1) / 2 * 5

    if discount >= 25: discount = 25

    discount_price = round(litres * (price_per_litre - discount / 100) , 2)

    return discount_price