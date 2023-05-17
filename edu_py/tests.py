products = {'Oranges (packaged)': 114.99, 'Candy (Rotfront)': 280.0, 'Boiled sausage': 199.99, 'Juice J7 (orange)': 119.99, 'Trout (Seven Seas)': 399.99}
stocks = {'Boiled sausage': '33%', 'Juice J7 (orange)': '12%', 'Trout (Seven Seas)': '18%'}

def apply_discounts(products, stocks):
    for key, val  in products.items():
        if key in stocks.keys():
            products[key] = round(products[key] - products[key]*int(stocks[key].replace('%', ''))/100, 2)
    return products
        
print(apply_discounts(products, stocks))