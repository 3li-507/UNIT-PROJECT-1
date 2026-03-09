# utils/currency_converter.py
def convert_amount(amount, from_currency, to_currency):
    """Convert amount between SAR and USD"""
    # 1 USD = 3.75 SAR 
    if from_currency == "SAR" and to_currency == "USD":
        return amount / 3.75
    elif from_currency == "USD" and to_currency == "SAR":
        return amount * 3.75
    #return same amount
    return amount