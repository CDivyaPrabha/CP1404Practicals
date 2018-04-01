no_of_items = int(input('Number of items: '))
while no_of_items <= 0:
    print('Invalid number of items! Enter again!')
    no_of_items = int(input('Number of items: '))
total_price = 0
for i in range(0, no_of_items, 1):
    price_of_item = float(input('Price of item:'))
    total_price = total_price + price_of_item
if total_price > 100:
    total_price = total_price - 10/100*total_price
total_price = round(total_price, 2)
print('Total price for', no_of_items, 'items is $', total_price)
