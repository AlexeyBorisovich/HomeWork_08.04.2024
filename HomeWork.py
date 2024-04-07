# В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


# ОТВЕТ: Мне кажется сможем.

# Мы импортируем библиотеку pandas.
import pandas as pd

# Генерируем исходные данные
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получем уникальные значения из столбца 'whoAmI'
categories = data['whoAmI'].unique()

# Создаем новый DataFrame для one hot
one_hot_data = pd.DataFrame(0, index=data.index, columns=categories)

# Заполняем значения one hot
for category in categories:
    one_hot_data[category] = (data['whoAmI'] == category).astype(int)

# Объединяем one hot DataFrame с исходным DataFrame
data_one_hot = pd.concat([data.drop(columns=['whoAmI']), one_hot_data], axis=1)

print(data_one_hot.head())