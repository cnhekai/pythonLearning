dictionary = {}
dictionary['one'] = 'this is one'
dictionary[2] = 'this is two'

tinydict = {'name':'hekai', 'job':'web','old':17}

print(dictionary['one']) # 输出键为'one'的值
print(dictionary[2]) # 输出键为2的值
print(tinydict) # 输出tinydict所有的值
print(tinydict.keys()) # 输出tinydict所有的键
print(tinydict.values()) # 输出tinydict所有的值

dictionary['addKey'] = 'addValue' # 添加一个key为addKey的键值对
print(dictionary.get('addKey')) # 打印新添加的key为addKey的值
dictionary.pop('addKey') # 删除key为addKey的键值对
print(dictionary.get('addKey',-1)) # 如果key不存在，可以返回None，或者自己指定的value