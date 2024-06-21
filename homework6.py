my_dict = {'Вася': 1975, 'Егор': 1999, 'Маша': 2002}
print('Dict', my_dict)
print('Existing value:', my_dict['Вася'])
print('Not existing value:', my_dict.get('Лера'))
my_dict.update({'Камила': 1981, 'Артем': 1915})
print('Modified dictionary:', my_dict)
a = my_dict.pop('Вася')
print('Deleted:', a)
print(my_dict)

my_set = {1, 2, 'ttt', 2, 1.2, 1.2, 'ttt'}
print('Set:', set(my_set))
my_set.add(4)
my_set.add(6)
my_set.discard('ttt')
print('Modified set:', my_set)
