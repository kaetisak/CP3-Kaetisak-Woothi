def vat_calculate(total_price):
    result = total_price+(total_price*7/100)
    return result

price = int(input())
print(vat_calculate(price))