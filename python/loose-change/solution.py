def loose_change(cents):
    if cents < 0:
        cents = 0
    
    coin_type = ['Quarters', 'Dimes', 'Nickels', 'Pennies']
    coin_value = [25, 10, 5, 1]

    def exact_coins(cents, value_coin):
        corresponding_coin, surplus = divmod(int(cents), value_coin)
        return corresponding_coin, surplus
    
    change_dict = {}
    for coin_name, value in zip(coin_type, coin_value):
        change_dict[coin_name], cents = exact_coins(cents, value)
    
    return change_dict