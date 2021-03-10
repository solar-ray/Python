goods = []
goods_properties = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
goods_counter = 0
feature = None
user_input = None
while True:
    user_input = input("Для выхода нажмите 'q', для продолжения -  'Enter': ")
    if user_input != 'q':
        goods_counter += 1
        for i in goods_properties.keys():
            feature = input(f'{i} товара: ')
            goods_properties[i] = int(feature) if (i == 'цена' or i == 'количество') else feature
            analytics[i].append(goods_properties[i])
            # Для аналитики оставляем только неповторяющиеся значения, как в примере в задании
            analytics[i] = list(set(analytics[i]))
        goods.append((goods_counter, goods_properties))
    else:
        break
print(f"Товары: {goods}\nАналитика: {analytics}")
