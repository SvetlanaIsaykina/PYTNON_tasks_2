# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]

prices_list = [65.2, 95, 56.45, 2, 105.2, 15.26, 56, 112.3, 26.3, 85, 69.02, 105.2]

# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

for price in prices_list:
  r = int(price)
  kk = (price - r) * 100
  print('{0} руб {1:02d} коп, '.format(r, int(kk)), end = " ")

# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
  
print(id(prices_list))
prices_list.sort()
for price in prices_list:
  r = int(price)
  kk = (price - r) * 100
  print('{0} руб {1:02d} коп, '.format(r, int(kk)))
print(id(prices_list))

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
sorted_prices = sorted(prices_list, reverse = True)
for price in sorted_prices:
  r = int(price)
  kk = (price - r) * 100
  print('{0} руб {1:02d} коп, '.format(r, int(kk)))
print(id(sorted_prices))

# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

top_five = sorted(sorted_prices[0:5])
for price in top_five:
  r = int(price)
  kk = (price - r) * 100
  print('{0} руб {1:02d} коп, '.format(r, int(kk)), end = " ")