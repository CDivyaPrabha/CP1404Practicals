my_dict = {'a': 2, 3: ['x', 'y'], 'joe': 'smith'}
dict_value_view = my_dict.values()
print(dict_value_view)
print(type(dict_value_view))
for val in dict_value_view:
    print(val)
my_dict['new_key'] = 'new_value'
print(dict_value_view)
dict_key_view = my_dict.keys()
print(dict_key_view)
print(dict_value_view)
