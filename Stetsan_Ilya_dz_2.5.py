import random

price_list = [round(random.uniform (1,100), 2) for i in range (20)]
print(id(price_list))
price_list.sort()
print(id(price_list))

revers_list = price_list.copy()[::-1]

def price(lists):
    new_list = []
    for el in lists:
        el = str(el)
        lists = el.split('.')
        strocke = f'{lists[0]} руб {lists[1]} коп'
        new_list.append(strocke)
    text = ', '.join(new_list)
    return text

print(price(price_list))
print(price(revers_list))
print(price(price_list[-5:]))
