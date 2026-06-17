def calculate_discount(total_purchase, order_amount):
    if total_purchase >= 50000000:
        return 0.1

    if total_purchase + order_amount >= 50000000:
        return 0.1
    return 0